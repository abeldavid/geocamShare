#!/usr/bin/python

import os
import uuid

from django.db import connection, transaction
from django.conf import settings

from geocamTrack.models import Track, Resource, IconStyle, LineStyle, \
     ResourcePosition, PastResourcePosition

@transaction.commit_manually
def renameCoreTables():
    cursor = connection.cursor()
    coreTables = ['assignment',
                  'change',
                  'folder',
                  'googleearthsession',
                  'operation',
                  'permission',
                  'sensor',
                  'snapshot',
                  'track',
                  'unit',
                  'unit_permissions',
                  'userprofile',
                  'userprofile_assignments',
                  'userprofile_userPermissions']
    for t in coreTables:
        cursor.execute("RENAME TABLE `shareCore_%s` TO `geocamCore_%s`;" % (t, t))
        transaction.commit()

@transaction.commit_manually
def renamePhotoTable():
    cursor = connection.cursor()
    cursor.execute("RENAME TABLE `shareGeocam_photo` TO `geocamLens_photo`;")
    transaction.commit()

@transaction.commit_manually
def renameTrackTables():
    cursor = connection.cursor()
    renameTables = ['resource',
                    'resourceposition',
                    'pastresourceposition']
    for t in renameTables:
        cursor.execute("RENAME TABLE `shareTracking_%s` TO `geocamTrack_%s`;" % (t, t))
        transaction.commit()

    # add new fields
    alterTables = ['resourceposition',
                   'pastresourceposition']
    fields = ["`track_id` int(11) DEFAULT NULL",
              "`heading` double DEFAULT NULL",
              "`precisionMeters` double DEFAULT NULL",
              "`uuid` varchar(48) NOT NULL"]
    for t in alterTables:
        for field in fields:
            cursor.execute("ALTER TABLE `geocamTrack_%s` ADD COLUMN %s;" % (t, field))
            transaction.commit()

    cursor.execute("ALTER TABLE `geocamTrack_resource` ADD COLUMN `extras` longtext NOT NULL;")
    transaction.commit()

@transaction.commit_manually
def renameLatitudeTable():
    cursor = connection.cursor()
    cursor.execute("RENAME TABLE `shareLatitude_latitudeprofile` TO `geocamTrack_latitudeprofile`;")
    transaction.commit()

@transaction.commit_manually
def addTracks():
    # create a Track object for each Resource
    resources = Resource.objects.all()
    iconStyle = IconStyle.objects.get(name='default')
    lineStyle = LineStyle.objects.get(name='default')
    trackLookup = {}
    for r in resources:
        t = Track(name=r.user.username,
                  resource=r,
                  iconStyle=iconStyle,
                  lineStyle=lineStyle)
        t.save()
        trackLookup[r.id] = t.id
    transaction.commit()

    # find the Track corresponding to each Resource and fill it in where
    # needed
    tables = ['geocamTrack_resourceposition',
              'geocamTrack_pastresourceposition']
    cursor = connection.cursor()
    for t in tables:
        cursor.execute('SELECT `id`, `resource_id` FROM `%s`;' % t)
        args = [(trackLookup[resource_id], str(uuid.uuid4()), id)
                for id, resource_id in cursor.fetchall()]
        cursor.executemany("UPDATE `%s` SET `track_id` = %%s, `uuid` = %%s WHERE `id` = %%s;" % t,
                           args)
        transaction.commit()

    # mark the track field not null and delete the resource field
    for t in tables:
        cursor.execute('ALTER TABLE `%s` MODIFY `track_id` int(11) NOT NULL;' % t)
        cursor.execute('ALTER TABLE `%s` DROP COLUMN `resource_id`;' % t)
    transaction.commit()

def migrate():
    renameCoreTables()
    renamePhotoTable()
    renameTrackTables()
    renameLatitudeTable()
    os.system('%s/manage.py syncdb' % settings.CHECKOUT_DIR)
    addTracks()

def main():
    import optparse
    parser = optparse.OptionParser('usage: %prog')
    opts, args = parser.parse_args()
    migrate()

if __name__ == '__main__':
    main()

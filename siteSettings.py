# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

import os

from geocamCore.baseSettings import *

USING_DJANGO_DEV_SERVER = ('runserver' in sys.argv)

ADMINS = (
    ('Trey Smith', 'info@geocamshare.org'),
)
MANAGERS = ADMINS

# django settings overrides for geocamDisasterStyle
INSTALLED_APPS = INSTALLED_APPS + (
    'geocamAware',
    'geocamLens',
    'geocamTrack',
    'geocamFolder'
    )

# GEOCAM_LENS_VIEW_MODULE = 'xgds_k10.ViewK10'

ROOT_URLCONF = 'geocamShare.urls'

# DIGEST_* -- settings for django_digest HTTP digest authentication
DIGEST_REALM = 'geocamshare.org'

# Email Settings, override these to ensure that invites are sent succesfully
EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

INVITE_SUBJECT = 'You have been invited to the %(groupname)s group'
INVITE_FROM = EMAIL_HOST_USER
INVITE_MESSAGE = """
Hello,

You have been invited to join the %(groupname)s on GeoCam.

To join this group click the link bellow and follow the instructions:

%(invitelink)s

Thank You,
The GeoCamTeam
"""

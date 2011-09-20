# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

from geocamCore.baseSettings import *  # pylint: disable=W0401

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
    )

# GEOCAM_LENS_VIEW_MODULE = 'xgds_k10.ViewK10'

ROOT_URLCONF = 'geocamShare.urls'

# DIGEST_* -- settings for django_digest HTTP digest authentication
DIGEST_REALM = 'geocamshare.org'

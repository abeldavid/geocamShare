# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

"""
settings.py -- Local site settings

Override in this what you wish.  By default it simply imports the
site default settings and overrides nothing.

This file should *not* be checked into git.
"""

import sys

from siteSettings import *

# Make this unique, and don't share it with anybody.  Used by Django's
# cookie-based authentication mechanism.
SECRET_KEY = '{{ secretKey }}'

GEOCAM_MEMO_GOOGLE_C2DM_TOKEN = 'fill in your key here -- get from http://code.google.com/android/c2dm/'

# Normally you don't need to set GOOGLE_MAPS_API_KEY, but it is required if
# you're using the alternate mapping backend based on the Google Earth
# API.
#GOOGLE_MAPS_API_KEY = 'fill in key for your domain here -- get from http://code.google.com/apis/maps/signup.html'

# For example, override the database settings:
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'dev.db'
#    }
#}

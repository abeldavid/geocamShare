# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

import django.conf

from geocamShare.shareCore.utils import MultiSettings
import defaultSettings

from client import LatitudeClient

settings = MultiSettings(django.conf.settings, defaultSettings)

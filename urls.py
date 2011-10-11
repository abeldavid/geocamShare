# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

from django.conf.urls.defaults import *  # pylint: disable=W0401
from django.conf import settings

from geocamCore.baseUrls import urlpatterns as basePatterns
from geocamCore.urls import urlpatterns as corePatterns
from geocamLens.ViewLensSimple import viewSingleton as lensViews

urlpatterns = (basePatterns
               + corePatterns
               + patterns(
    '',

    (r'^geocamAware/', include('geocamAware.urls')),
    (r'^geocamLens/', include('geocamLens.urls')),
    (r'^geocamTrack/', include('geocamTrack.urls')),
    (r'^geocamMemo/', include('geocamMemo.urls')),
    (r'^geocamTalk/', include('geocamTalk.urls')),

    # normally we would put this url in the geocamLens namespace, but 
    # the current version of GeoCam Mobile expects it at the top level
    (r'^upload-m/$', lensViews.uploadImageAuth,
     {'challenge': 'basic'}),

    (r'^$', 'django.views.generic.simple.redirect_to',
     {'url': settings.SCRIPT_NAME + 'geocamAware/',
      'readOnly': True}
     ),
))

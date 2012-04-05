# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

from django.conf.urls.defaults import *  # pylint: disable=W0401
from django.conf import settings
from django.contrib import admin

from geocamLens.ViewLensSimple import viewSingleton as lensViews
from geocamCore import views

urlpatterns = patterns(
    '',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^$', views.welcome),

    url(r'^accounts/register/$', views.register,
        {'loginRequired': False},
        name='register'),

    # accounts
    url(r'^accounts/login/$', views.welcome, # 'django.contrib.auth.views.login',
        {'loginRequired': False,  # avoid redirect loop
         'securityTags': ['loginRelated']
         },
        name='geocamCore_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        # show logout page instead of redirecting to log in again
        {'loginRequired': False,
         'securityTags': ['loginRelated']
         }),

    url(r'^m/checkLogin/$', views.checkLogin,
        {'challenge': 'basic',
         'securityTags': ['dumbClient']},
        name='geocamCore_checkLogin'),

    url(r'^m/register/$', views.register,
        {'loginRequired': False,
         'securityTags': ['loginRelated'],
         'useJson': True},
        name='geocamCore_register'),

    url(r'^geocamAware/', include('geocamAware.urls')),
    url(r'^geocamLens/', include('geocamLens.urls')),
    url(r'^geocamTrack/', include('geocamTrack.urls')),
    url(r'^geocamMemo/', include('geocamMemo.urls')),
    url(r'^geocamTalk/', include('geocamTalk.urls')),

    # normally we would put this url in the geocamLens namespace, but 
    # the current version of GeoCam Mobile expects it at the top level
    url(r'^upload-m/$', lensViews.uploadImageAuth,
        {'challenge': 'basic'}),
)

if settings.USE_STATIC_SERVE:
    urlpatterns += patterns(
        '',

        url(r'^media/(?P<path>.*)$',
            'geocamUtil.views.staticServeWithExpires.staticServeWithExpires',
            dict(document_root=settings.MEDIA_ROOT,
                 show_indexes=True,
                 readOnly=True)),
        
        url(r'^data/(?P<path>.*)$',
            'geocamUtil.views.staticServeWithExpires.staticServeWithExpires',
            {'document_root': settings.DATA_DIR,
             'show_indexes': True,
             'readOnly': True}),

        url(r'^favicon.ico$', 'django.views.generic.simple.redirect_to',
            {'url': settings.MEDIA_URL + 'geocamCore/icons/camera.ico',
             'readOnly': True}),
        )

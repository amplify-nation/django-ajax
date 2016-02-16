from django.conf.urls import patterns, url, include
from django.views.static import serve

from . import views
import os

JAVASCRIPT_PATH = "%s/js" % os.path.dirname(__file__)

urlpatterns = [
    url(r'^(?P<application>\w+)/(?P<model>\w+).json', views.endpoint_loader),
    url(r'^(?P<application>\w+)/(?P<model>\w+)/(?P<method>\w+).json', views.endpoint_loader),
    url(r'^(?P<application>\w+)/(?P<model>\w+)/(?P<pk>\d+)/(?P<method>\w+)/?(?P<taggit_command>(add|remove|set|clear|similar))?.json$', views.endpoint_loader),
    url(r'^js/(?P<path>.*)$', serve, {'document_root': JAVASCRIPT_PATH}),
]

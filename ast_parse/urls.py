from django.conf.urls import patterns, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'', include('ast_parse.parse.urls', namespace='parse', app_name='parse')),
)

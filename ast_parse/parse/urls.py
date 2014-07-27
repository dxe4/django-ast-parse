from django.conf.urls import patterns, url

urlpatterns = patterns(
    'ast_parse.parse.views',
    url(r'^modules/all/?(?:(?P<is_json>json+)/?)?$',
        'all_modules', {}, name='all_modules'),
)

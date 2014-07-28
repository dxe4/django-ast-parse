from django.conf.urls import patterns, url

urlpatterns = patterns(
    'ast_parse.parse.views',
    url(r'^module/all/?(?:(?P<is_json>json+)/?)?$',
        'all_modules', {}, name='all_modules'),
    # TODO generate ids
    url(r'module(?P<path>(/[a-zA-Z_]+)+)+/?(?:(?P<is_json>json+)/?)?$',
        'module', name='module'),
)

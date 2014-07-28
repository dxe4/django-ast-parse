from django.conf.urls import patterns, url

# Maybe this design is better http://www.reddit.com/dev/api#GET_api_me.json

urlpatterns = patterns(
    'ast_parse.parse.views',
    url(r'^module/all/?(?:(?P<is_json>json+)/?)?$',
        'all_modules', {}, name='all_modules'),
    # TODO generate ids, good luck reading this regex 1 year from now
    url(r'module(?P<path>(/[a-zA-Z_]+)+)+/?(?:(?P<is_json>json+)/?)?$',
        'module', name='module'),
)

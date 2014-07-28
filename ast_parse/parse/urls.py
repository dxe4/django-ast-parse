from django.conf.urls import patterns, url

# Maybe this design is better http://www.reddit.com/dev/api#GET_api_me.json

urlpatterns = patterns(
    'ast_parse.parse.views',
    url(r'^package/all/?(?:(?P<is_json>json+)/?)?$',
        'all_packages_view', {}, name='all_modules'),
    # TODO generate ids, good luck reading this regex 1 year from now
    url(r'package(?P<path>(/[a-zA-Z_]+)+)+/?(?:(?P<is_json>json+)/?)?$',
        'package_view', name='package'),
)

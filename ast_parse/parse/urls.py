from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'all_modules', {}, name='all_modules'),
)

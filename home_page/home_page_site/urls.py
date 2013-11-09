#Standard Library
import os
#Django
from django.conf.urls import patterns, url
from django.conf import settings
#home_page
from home_page_app.views import main, contact


urlpatterns = patterns('',
    url(r'^$', main),
    url(r'^home*$', main),
    url(r'^contact*$', contact)
)

if settings.DEBUG:
    STATIC_PATH = os.path.join(os.path.dirname(__file__), "static", "one_files", "HTML")
    urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_PATH})
)

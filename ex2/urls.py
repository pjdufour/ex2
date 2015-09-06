from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home', name='home'),
    url(r'^hotspots/(?P<hotspot>[^/]+)$', 'hotspot_detail', name='hotspot_detail'),
    url(r'^about$', 'about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
)

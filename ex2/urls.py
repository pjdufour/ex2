from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from djgeojson.views import TiledGeoJSONLayerView

from .models import Country
from . import views 

admin.autodiscover()

urlpatterns = patterns('ex2.views',
    url(r'^$', views.home),

    url(r'^hotspots/(?P<hotspot>[^/]+)$', 'hotspot_detail', name='hotspot_detail'),

    url(r'^api/country/countries.geojson$', 'country_geojson', name='country_geojson_all'),
    url(r'^api/country/hotspot_(?P<hotspot>[^/]+).geojson$', 'country_geojson_contains', name='country_geojson_contains'),
    url(r'^api/hotspots/hotspot_all.geojson$', 'hotspot_geojson', name='hotspot_geojson_all'),
    url(r'^api/hotspots/hotspot_(?P<hotspot>[^/]+).geojson$', 'hotspot_geojson', name='hotspot_geojson_feature'),

    url(r'^api/vt/countries/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$',
        TiledGeoJSONLayerView.as_view(model=Country), name='vt_country'),

    url(r'^about$', 'about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
)

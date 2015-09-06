from django.core.serializers import serialize
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings

from .models import Country, HotSpot


def about(request, template="about.html"):
    ctx = {
        'SITEURL': settings.SITEURL
    }
    return render_to_response(
        template,
        RequestContext(request, ctx))


def home(request, template="home.html"):
    ctx = {
        'SITEURL': settings.SITEURL
    }
    return render_to_response(
        template,
        RequestContext(request, ctx))


def hotspot_detail(request, hotspot=None, template="hotspot_detail.html"):

    if request.method == "POST":
        return None
    else:
        instance = HotSpot.objects.get(id=hotspot)
        ctx = {
            'hotspot': instance,
            'center': str(list(reversed([coord for coord in instance.point])))
        }
        return render_to_response(
            template,
            RequestContext(request, ctx))


def hotspot_geojson(request, hotspot=None):

    if request.method == "POST":
        return None
    else:
        qs = HotSpot.objects.filter(id=hotspot) if hotspot else HotSpot.objects.all()[:400]
        import geojson
        hs_list = []
        for hs in qs:
            g = geojson.Point([coord for coord in hs.point])
            p = {
                'id': hs.id,
                'scan': hs.scan,
                'track': hs.track,
                'acq_date': str(hs.acq_date),
                'acq_time': hs.acq_time,
                'satellite': hs.satellite,
                'url': "/hotspots/{id}".format(id=hs.id)
            }
            f = geojson.Feature(geometry=g, properties=p)
            hs_list.append(f)
        out = geojson.dumps(geojson.FeatureCollection(hs_list))
        return HttpResponse(out, content_type="application/json")


def country_geojson(request, iso3=None):

    if request.method == "POST":
        return None
    else:
        qs = Country.objects.filter(iso3=iso3) if iso3 else Country.objects.all()

        country_dict = serialize(
            'geojson',
             qs,
             geometry_field='mpoly',
             fields=('mpoly', 'name', 'iso2', 'iso3', 'pop2005',))

        return HttpResponse(
            str(country_dict),
            content_type="application/json")


def country_geojson_contains(request, hotspot=None):

    if request.method == "POST":
        return None
    else:
        hs = HotSpot.objects.get(id=hotspot)
        qs = Country.objects.filter(mpoly__contains=hs.point)

        country_dict = serialize(
            'geojson',
             qs,
             geometry_field='mpoly',
             fields=('mpoly', 'name', 'iso2', 'iso3', 'pop2005',))

        return HttpResponse(
            str(country_dict),
            content_type="application/json")


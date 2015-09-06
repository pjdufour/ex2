import json, os, datetime

from django.shortcuts import render_to_response, get_object_or_404, render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.core.cache import cache, caches, get_cache

import StringIO
from PIL import Image, ImageEnhance
import umemcache

from .models import Country, HotSpot

import json
from bson.json_util import dumps

from geojson import Polygon, Feature, FeatureCollection, GeometryCollection

import time

def home(request, template="home.html"):
    ctx = {'SITEURL': settings.SITEURL, }
    return render(request, template, ctx, 'text/html')

def hotspot_detail(request, hotspot=None, template="hotspot_detail.html"):

    if request.method == "POST":
        return None
    else:
        instance = HotSpot.objects.get(id=hotspot)
        context_dict = {
            'hotspot': instance,
        }
        return render_to_response(
            template,
            RequestContext(request, context_dict))

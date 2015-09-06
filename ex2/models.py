import datetime
import logging
import os
import io
import sys
import uuid
from base64 import b64encode
from optparse import make_option
import json
import argparse
import time
import os
import subprocess
import binascii
import re

# from django.db import models
from django.db.models import signals
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from django.contrib.gis.db import models

class Country(models.Model):

    name = models.CharField('Name', max_length=400)
    iso2 = models.CharField('ISO 2', max_length=2)
    iso3 = models.CharField('ISO 3', max_length=3)
    pop2005 = models.IntegerField('2005 Population', default=0)

    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("name","iso2","iso3")
        verbose_name_plural = _("Countries")


class HotSpot(models.Model):

    scan = models.FloatField('Scan')
    track = models.FloatField('Scan')
    acq_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    satellite = models.CharField('Satellite', max_length=1)

    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("acq_date","scan","track","satellite")
        verbose_name_plural = _("Hot Spots")


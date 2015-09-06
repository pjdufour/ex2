from django.utils.translation import ugettext_lazy as _

from django.contrib.gis.db import models

class Country(models.Model):

    name = models.CharField('Name', max_length=400, null=True)
    iso2 = models.CharField('ISO 2', max_length=2, null=True)
    iso3 = models.CharField('ISO 3', max_length=3, null=True)
    pop2005 = models.IntegerField('2005 Population', default=0, null=True)

    mpoly = models.MultiPolygonField('Multi-polygon', srid=4326, null=True)
    objects = models.GeoManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("name", "iso2", "iso3")
        verbose_name_plural = _("Countries")


class HotSpot(models.Model):

    id = models.AutoField('ID', primary_key=True)
    scan = models.FloatField('Scan', null=True)
    track = models.FloatField('Track', null=True)
    acq_date = models.DateField('Acquisition Date',
        max_length=100, null=True, blank=True)
    acq_time = models.CharField('Acquisition Time',
        max_length=100, null=True, blank=True)
    satellite = models.CharField('Satellite',
        max_length=1, null=True)

    point = models.PointField('Point', null=True)
    objects = models.GeoManager()

    def __str__(self):
        return str(self.acq_date)+" "+str(self.acq_time)+"; "+self.satellite

    def __unicode__(self):
        return str(self.acq_date)+" "+str(self.acq_time)+"; "+self.satellite

    class Meta:
        ordering = ("id",)
        verbose_name_plural = _("Hot Spots")

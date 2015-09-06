from django.conf import settings
from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand
from optparse import make_option
import traceback
import datetime

from ex2.enumerations import COUNTRY_MAPPING
from ex2.models import Country

class Command(BaseCommand):

    help = ("Imports countries data.")

    args = 'path [path...]'

    option_list = BaseCommand.option_list + (
        make_option(
            '--source',
            dest="source",
            default=None,
            help="Source table name."),
    )

    def handle(self, *args, **options):
        verbose = options.get('verbose')
        source = options.get('source')

        if verbose:
            console = self.stdout
        else:
            console = None

        if not source:
            print "Source must be specified"
            return 0

        from django.contrib.gis.gdal import DataSource
        ds = DataSource("PG:host=localhost port=5432 dbname=ex1 user=ex1 password=ex1")

        lyr_ind = -1
        for i in range(len(ds)):
            if str(ds[i])  == source:
                lyr_ind = i
                break

        if lyr_ind == -1:
            print "Could not find table in data source"
            return 0

        lm = LayerMapping(Country, ds, COUNTRY_MAPPING, layer=lyr_ind, encoding='iso-8859-1')
        lm.save(strict=True, verbose=verbose)

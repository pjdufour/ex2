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
        make_option(
            '-o',
            '--overwrite',
            dest='overwrite',
            default=False,
            action="store_true",
            help="Overwrite existing data"),
    )

    def handle(self, *args, **options):
        verbose = options.get('verbose')
        source = options.get('source')
        overwrite = options.get('overwrite')

        if verbose:
            console = self.stdout
        else:
            console = None

        if not source:
            print "Source must be specified"
            return 0

        from django.contrib.gis.gdal import DataSource
        ds = DataSource("PG:host=localhost port=5432 dbname=ex1 user=ex1 password=ex1")
	print(ds)

        lyr_ind = -1
        for i in range(len(ds)):
            if str(ds[i])  == source:
                lyr_ind = i
                break

        lyr = ds[lyr_ind]
        print lyr
        print lyr.srs
        print lyr.geom_type
        print lyr.fields

        if lyr_ind == -1:
            print "Could not find table in data source"
            return 0

        print "Layer Index: ",lyr_ind
        lm = LayerMapping(Country, ds, COUNTRY_MAPPING, layer=lyr_ind, encoding='iso-8859-1')
        lm.save(strict=True, verbose=verbose)

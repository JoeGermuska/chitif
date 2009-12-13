"""
"""
from django.core.management.base import BaseCommand, CommandError, handle_default_options
from optparse import make_option
from django.contrib.gis.utils import LayerMapping
from geo.models import TIF, tif_mapping
import os.path
    
class Command(BaseCommand):
    args=''
    help=''
    option_list= BaseCommand.option_list + ()

    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        shapefile = "../data/gis/tifs/tifs.shp"
        lm = LayerMapping(TIF, shapefile, tif_mapping,
                          transform=False, encoding='iso-8859-1')
        
        lm.save(strict=True, verbose=True)

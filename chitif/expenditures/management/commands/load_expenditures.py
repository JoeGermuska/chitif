"""
"""
from django.core.management.base import BaseCommand, CommandError, handle_default_options
from optparse import make_option
import csv
from geo.models import TIF
from expenditures.models import Expenditure
    
class Command(BaseCommand):
    args=''
    help=''
    option_list= BaseCommand.option_list + ()

    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        data = open("../data/Expenditure_Data_With_TIF_ID.csv","U")
        r = csv.reader(data)
        headers = r.next()
        for district,area,expire,expend,year,status,amt,balance,ref in r:
            try:
                if ref:
                    amt = amt.replace(",","")
                    tif = TIF.objects.get(ref=ref)
                    e = Expenditure(tif=tif,description=expend,year=year,status=status,amount=amt)
                    e.save()
            except TIF.DoesNotExist:
                print "%s does not exist" % ref    
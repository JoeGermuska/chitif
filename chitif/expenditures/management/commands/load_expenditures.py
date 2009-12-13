"""
"""
from django.core.management.base import BaseCommand, CommandError, handle_default_options
from optparse import make_option
import csv
from geo.models import TIF
from expenditures.models import Expenditure
from datetime import datetime
    
class Command(BaseCommand):
    args=''
    help=''
    option_list= BaseCommand.option_list + ()

    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        data = open("../data/Expenditure_Data_With_TIF_ID.csv","U")
        last_tif = None
        display_order = 0
        r = csv.reader(data)
        headers = r.next()
        for district,area,expire,expend,year,status,amt,balance,ref in r:
            try:
                if ref:
                    amt = amt.replace(",","")
                    balance = balance.replace(",","")
                    tif = TIF.objects.get(ref=ref)
                    if tif != last_tif:
                        last_tif = tif
                        tif.region = area
                        tif.expiration_date = self.make_date(expire)
                        tif.save()
                        display_order = 0
                    else:
                        display_order += 1
                    e = Expenditure(tif=tif,description=expend,year=year,status=status,amount=amt,display_order=display_order,balance=balance)
                    e.save()
            except TIF.DoesNotExist:
                print "%s does not exist" % ref

    def make_date(self,str):
        return datetime.strptime(str,"%m/%d/%y")


from django.views.decorators.cache import cache_page
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.gis.shortcuts import render_to_kml
from django.http import HttpResponse
from django.conf import settings
from expenditures.models import Expenditure
from geo.models import TIF

# Create your views here.

def home(request):
    tifs = TIF.objects.all()
    return render_to_response("expenditures/index.html", {'tifs': tifs})
  
def home_kml(request):
    tifs = TIF.objects.kml()
    return render_to_kml("expenditures/placemarks.kml",{'places' : tifs})
    
def tif(request, tif_slug):
    tif = get_object_or_404(TIF,slug=tif_slug)
    expenditures = Expenditure.objects.filter(tif__slug=tif_slug)
    context = {'expenditures': expenditures, 'tif': tif}
    return render_to_response("expenditures/tif.html", context)

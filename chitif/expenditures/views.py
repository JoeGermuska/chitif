from django.views.decorators.cache import cache_page
from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string
from django.contrib.gis.shortcuts import render_to_kml
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

def home(request):
    return render_to_response("expenditures/index.html", {})
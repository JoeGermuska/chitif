from django.conf.urls.defaults import *
from expenditures import views as expenditures_views
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    url("^tif/(?P<tif_slug>[\w-]+)/",
        expenditures_views.tif,
        name="tif"),
    (r'^tifs.kml', expenditures_views.home_kml),
    (r'^expenditures/', include('expenditures.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    (r'', expenditures_views.home),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

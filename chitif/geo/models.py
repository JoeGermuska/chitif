from django.contrib.gis.db import models

# Create your models here.
# initially generated using
# python ./manage.py ogrinspect ../data/gis/tifs/tifs.shp TIF --name NAME --mapping --multi --srid=102671
# but edited a little

# Remember: Chicago GIS data is usually in a specialized projection
#   (NAD 1983 StatePlane Illinois East FIPS 1201 Feet)
# http://spatialreference.org/ref/esri/102671/
# You may need to add this projection to your PostGIS database
# INSERT INTO "spatial_ref_sys" ("srid", "auth_name", "auth_srid", "srtext", "proj4text")
# VALUES (102671, 'ESRI', 102671, 'PROJCS[\"NAD_1983_StatePlane_Illinois_East_FIPS_1201_Feet\",GEOGCS[\"GCS_North_American_1983\",DATUM[\"D_North_American_1983\",SPHEROID[\"GRS_1980\",6378137,298.257222101]],PRIMEM[\"Greenwich\",0],UNIT[\"Degree\",0.017453292519943295]],PROJECTION[\"Transverse_Mercator\"],PARAMETER[\"False_Easting\",984249.9999999999],PARAMETER[\"False_Northing\",0],PARAMETER[\"Central_Meridian\",-88.33333333333333],PARAMETER[\"Scale_Factor\",0.999975],PARAMETER[\"Latitude_Of_Origin\",36.66666666666666],UNIT[\"Foot_US\",0.30480060960121924]]', '+proj=tmerc +lat_0=36.66666666666666 +lon_0=-88.33333333333333 +k=0.999975 +x_0=300000 +y_0=0 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192');
# This is an auto-generated Django model module created by ogrinspect.
#
class TIF(models.Model):
    name = models.CharField(max_length=55)
    ref = models.CharField(max_length=10)
    ind = models.CharField(max_length=20)
    use = models.CharField(max_length=50)
    show = models.IntegerField()
    area = models.FloatField()
    perimiter = models.FloatField()
    geom = models.MultiPolygonField(srid=102671)
    objects = models.GeoManager()

    def __unicode__(self): return self.name

# Auto-generated `LayerMapping` dictionary for TIF model
tif_mapping = {
    'ref' : 'REF',
    'ind' : 'IND',
    'use' : 'USE',
    'show' : 'SHOW',
    'name' : 'NAME_TRIM',
    'area' : 'AREA',
    'perimiter' : 'LEN',
    'geom' : 'MULTIPOLYGON',
}

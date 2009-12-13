from django.db import models
from geo.models import TIF
# Create your models here.

class Expenditure(models.Model):
    """Data from Chicago Reader FOIA"""
    tif = models.ForeignKey(TIF)
    description = models.CharField(blank=False, max_length=90)
    year = models.IntegerField(null=False)
    status = models.CharField(blank=True, max_length=15)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = []
        verbose_name, verbose_name_plural = "", "s"

    def __unicode__(self):
        return u"Expenditure"

    @models.permalink
    def get_absolute_url(self):
        return ('Expenditure', [self.id])
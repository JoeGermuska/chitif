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
    balance = models.IntegerField(blank=True, null=True,help_text="Balance after line item, as represented in data import. May be redundant to computed values.")
    display_order = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = []
        verbose_name, verbose_name_plural = "", "s"

    def __unicode__(self):
        return u"[%s] %s" % (self.tif.name,self.description)

    @models.permalink
    def get_absolute_url(self):
        return ('expenditure', [self.id])
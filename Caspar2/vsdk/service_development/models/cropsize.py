import requests
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CropSize(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Crop size')
        verbose_name_plural = 'Crop sizes'

    def __str__(self):
        return self.name

    def save(self):

        super(CropSize, self).save()

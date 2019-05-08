import requests
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Crop(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Crop')
        verbose_name_plural = 'Crops'

    def __str__(self):
        return self.name

    def save(self):

        super(Crop, self).save()

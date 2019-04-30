import requests
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Village(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Village')
        verbose_name_plural = 'Villages'

    def __str__(self):
        return self.name

    def save(self):
        # if not self.id:
        #     self.latitude = 1
        #     self.longitude = 2
        self.updated = datetime.datetime.today()
        super(Village, self).save()

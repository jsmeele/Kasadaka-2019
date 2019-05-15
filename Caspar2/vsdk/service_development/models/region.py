import requests
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey('VoiceLabel',
                                    blank = True,
                                    null = True,
                                    on_delete = models.PROTECT,
                                    verbose_name = _('Region voice label'),
                                    related_name = 'region_description_voice_label',
                                    help_text = _("A Voice Label of the name of the language"))

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name

    def save(self):

        super(Region, self).save()

    @property
    def get_region_voice_label_url(self):
        """
        Returns a Region hardcoded interface audio fragments.
        """
        return self.region.get_voice_fragment_url2(self)

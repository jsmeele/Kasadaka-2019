import requests
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Village(models.Model):
    name = models.CharField(max_length=50)
    village = models.ForeignKey('VoiceLabel',
                                blank = True,
                                null = True,
                                on_delete = models.PROTECT,
                                verbose_name = _('Village voice label'),
                                related_name = 'village_description_voice_label',
                                help_text = _("A Voice Label of the name of the village"))

    class Meta:
        verbose_name = _('Village')
        verbose_name_plural = 'Villages'

    def __str__(self):
        return self.name

    # def save(self):
    #
    #     super(Village, self).save()

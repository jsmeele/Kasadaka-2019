from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.utils.safestring import mark_safe

from ..models import Region


class VoiceLabel(models.Model):
    name = models.CharField(_('Name'),max_length=50)
    description = models.CharField(_('Description'),max_length=1000, blank = True, null = True)

    class Meta:
        verbose_name = _('Voice Label')

    def __str__(self):
        return _("Voice Label") + ": %s" % (self.name)

    def is_valid(self):
        return len(self.validator()) == 0
    is_valid.boolean = True
    is_valid.short_description = _('Is valid')

    def validator(self, language):
        errors = []
        if len(self.voicefragment_set.filter(language = language)) > 0:
            errors.extend(self.voicefragment_set.filter(language=language)[0].validator())
        else:
            errors.append(ugettext('"%(description_of_this_element)s" does not have a Voice Fragment for "%(language)s"') %{'description_of_this_element' : str(self),'language' : str(language)})
        return errors

    def get_voice_fragment_url(self, language):
        # print('+++++++++++VOICE_LABEL++++++++++++')
        # print(self.voicefragment_set.filter(language=language)[0])
        return self.voicefragment_set.filter(language=language)[0].get_url()

    def get_voice_fragment_url2(self, language):
        # print('+++++++++++VOICE_LABEL2++++++++++++')
        # print(language)
        # print(Region.voicefragment_set)
        return 'TEST' #self.voicefragment_set.filter(language=language)[0].get_url()

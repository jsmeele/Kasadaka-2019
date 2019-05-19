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
                               help_text = _("A Voice Label of the name of the region"))

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name

    # def is_valid(self):
    #     return len(self.validator()) == 0
    # is_valid.boolean = True
    # is_valid.short_description = _('Is valid')
    #
    # def validator(self):
    #     """
    #     Returns a list of problems with this element that would surface when accessing
    #     through voice.
    #     """
    #     errors = []
    #     #check if voice label is present, and validate it
    #     if self.region:
    #         for language in self.service.supported_languages.all():
    #             errors.extend(self.region.validator(language))
    #     else:
    #         errors.append(ugettext('No VoiceLabel in: "%s"')%str(self))
    #     return errors
    # @property
    # def get_voice_fragment_url(self, session): #, language):
    #     """
    #     Returns the url of the audio file of this element, in the given language.
    #     """
    #     print('###### TEST #####')
    #     return '9999999' #self.region.get_voice_fragment_url(language)

    # def save(self):
    #
    #     super(Region, self).save()

    # @property
    # def get_region_voice_label_url(self):
    #     """
    #     Returns a Region hardcoded interface audio fragments.
    #     """
    #     return self.region.get_voice_fragment_url2(self)

####### START ################## WORKING TEST ####
    # @property
    # def get_region_voice_label_url(self):
    #     """
    #     Returns a dictionary containing all URLs of Voice
    #     Fragments of the hardcoded interface audio fragments.
    #     """
    #     # language2 = session.language
    #     language = 1 #'English (en)'
    #     # interface_voice_labels = {
    #     #         'region':self.region,
    #     #         }
    #     # for k, v in interface_voice_labels.items():
    #     #     interface_voice_labels[k] = v.get_voice_fragment_url(self)
    #     print('XYZ__111__ZYX')
    #     # print(self)
    #     # print(self.region.get_voice_fragment_url(self))  # .voicefragment_set.filter(*)[0].get_url())
    #     # print(CallSession.language)
    #     # print(len(VoiceLabel.object.all()))
    #     url = self.region.voicefragment_set.filter(language=language)[0].get_url()
    #     print(url)
    #     print(self)
    #     return url #'TEST123---XYZ__111__ZYX'  #interface_voice_labels
####### END ################## WORKING TEST ####

    # @property
    # def get_description_voice_label_url(self):
    #     """
    #     Returns the URL of the Voice Fragment describing
    #     the language, in the language itself.
    #     """
    #     return self.voice_label.get_voice_fragment_url(self)

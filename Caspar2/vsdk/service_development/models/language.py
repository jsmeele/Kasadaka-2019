from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.utils.safestring import mark_safe

class Language(models.Model):
    name = models.CharField(_('Name'),max_length=100, unique = True)
    code = models.CharField(_('Code'),max_length=10, unique = True)
    voice_label = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = _('Language voice label'),
            related_name = 'language_description_voice_label',
            help_text = _("A Voice Label of the name of the language"))
    error_message = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = _('Error message voice label'),
            related_name = 'language_error_message',
            help_text = _("A general error message"))
    select_language = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = _('Select language voice label'),
            related_name = 'language_select_language',
            help_text = _("A message requesting the user to select a language"))
    pre_choice_option = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = _('Pre-Choice Option voice label'),
            related_name = 'language_pre_choice_option',
            help_text = _("The fragment that is to be played before a choice option (e.g. '[to select] option X, please press 1')"))
    post_choice_option = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = _('Post-Choice Option voice label'),
            related_name = 'language_post_choice_option',
            help_text = _("The fragment that is to be played before a choice option (e.g. 'to select option X, [please press] 1')"))
    one = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = ugettext("The number %(number)s")% {'number':'1'},
            related_name = 'language_one',
            help_text = ugettext('The number %(number)s')% {'number':'1'})
    two = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = ugettext("The number %(number)s")% {'number':'2'},
            related_name = 'language_two',
            help_text = ugettext("The number %(number)s")% {'number':'2'})
    three = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = ugettext("The number %(number)s")% {'number':'3'},
            related_name = 'language_three',
            help_text = ugettext("The number %(number)s")% {'number':'3'})
    four = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = ugettext("The number %(number)s")% {'number':'4'},
            related_name = 'language_four',
            help_text = ugettext("The number %(number)s")% {'number':'4'})
    five = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = ugettext("The number %(number)s")% {'number':'5'},
            related_name = 'language_five',
            help_text = ugettext("The number %(number)s")% {'number':'5'})
    six = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = ugettext("The number %(number)s")% {'number':'6'},
            related_name = 'language_six',
            help_text = ugettext("The number %(number)s")% {'number':'6'})
    seven = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = ugettext("The number %(number)s")% {'number':'7'},
            related_name = 'language_seven',
            help_text = ugettext("The number %(number)s")% {'number':'7'})
    eight = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = ugettext("The number %(number)s")% {'number':'8'},
            related_name = 'language_eight',
            help_text = ugettext("The number %(number)s")% {'number':'8'})
    nine = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = ugettext("The number %(number)s")% {'number':'9'},
            related_name = 'language_nine',
            help_text = ugettext("The number %(number)s")% {'number':'9'})
    zero = models.ForeignKey('VoiceLabel',
            on_delete = models.PROTECT,
            verbose_name = ugettext("The number %(number)s")% {'number':'0'},
            related_name = 'language_zero',
            help_text = ugettext("The number %(number)s")% {'number':'0'})

    class Meta:
        verbose_name = _('Language')

    def __str__(self):
        return '%s (%s)' % (self.name, self.code)

    @property
    def get_description_voice_label_url(self):
        """
        Returns the URL of the Voice Fragment describing
        the language, in the language itself.
        """
        return self.voice_label.get_voice_fragment_url(self)

    @property
    def get_interface_numbers_voice_label_url_list(self):
        numbers = [
                    self.zero,
                    self.one,
                    self.two,
                    self.three,
                    self.four,
                    self.five,
                    self.six,
                    self.seven,
                    self.eight,
                    self.nine
                    ]
        result = []
        for number in numbers:
            result.append(number.get_voice_fragment_url(self))
        return result

    @property
    def get_interface_voice_label_url_dict(self):
        """
        Returns a dictionary containing all URLs of Voice
        Fragments of the hardcoded interface audio fragments.
        """
        interface_voice_labels = {
                'voice_label':self.voice_label,
                'error_message':self.error_message,
                'select_language':self.select_language,
                'pre_choice_option':self.pre_choice_option,
                'post_choice_option':self.post_choice_option,
                }
        for k, v in interface_voice_labels.items():
            interface_voice_labels[k] = v.get_voice_fragment_url(self)
        return interface_voice_labels

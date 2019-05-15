from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.utils.safestring import mark_safe

from .validators import validate_audio_file_extension, validate_audio_file_format

class VoiceFragment(models.Model):
    parent = models.ForeignKey('VoiceLabel',
            on_delete = models.CASCADE)
    language = models.ForeignKey(
            'Language',
            on_delete = models.CASCADE)
    audio = models.FileField(_('Audio'),
            validators=[validate_audio_file_extension],
            help_text = _("Ensure your file is in the correct format! Wave (.wav) : Sample rate 8KHz, 16 bit, mono, Codec: PCM 16 LE (s16l)"))


    class Meta:
        verbose_name = _('Voice Fragment')

    def convert_wav_to_correct_format(self):
        from vsdk import settings
        if not settings.KASADAKA:
            pass

        import subprocess
        from os.path import basename
        new_file_name = self.audio.path[:-4] + "_conv.wav"
        subprocess.getoutput("sox -S %s -r 8k -b 16 -c 1 -e signed-integer %s"% (self.audio.path, new_file_name))
        self.audio = basename(new_file_name)




    def save(self, *args, **kwargs):
        super(VoiceFragment, self).save(*args, **kwargs)
        from vsdk import settings
        if  settings.KASADAKA:
            format_correct = validate_audio_file_format(self.audio)
            if not format_correct:
                self.convert_wav_to_correct_format()
        super(VoiceFragment, self).save(*args, **kwargs)




    def __str__(self):
        return _("Voice Fragment: (%(name)s) %(name_parent)s") % {'name' : self.language.name, 'name_parent' : self.parent.name}

    def get_url(self):
        return self.audio.url

    def validator(self):
        errors = []
        #Temporary for ICT4D 2018, Heroku performance optimalization
        return errors
        try:
            accessible = self.audio.storage.exists(self.audio.name)
        except NotImplementedError:
            import urllib.request
            try:
                response = urllib.request.urlopen(self.audio.url)
                accessible = True
            except urllib.error.HTTPError:
                accessible = False


        if not self.audio:
            errors.append(ugettext('%s does not have an audio file')%str(self))
        elif not accessible:
            errors.append(ugettext('%s audio file not accessible')%str(self))
        #TODO verift whether this really is not needed anymore
        #elif not validate_audio_file_format(self.audio):
        #    errors.append(ugettext('%s audio file is not in the correct format! Should be: Wave: Sample rate 8KHz, 16 bit, mono, Codec: PCM 16 LE (s16l)'%str(self)))
        return errors

    def is_valid(self):
        return len(self.validator()) == 0
    is_valid.boolean = True
    is_valid.short_description = _('Is valid')

    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio:
            file_url = settings.MEDIA_URL + str(self.audio)
            player_string = str('<audio src="%s" controls>'  % (file_url) + ugettext('Your browser does not support the audio element.') + '</audio>')
            return mark_safe(player_string)

    audio_file_player.short_description = _('Audio file player')

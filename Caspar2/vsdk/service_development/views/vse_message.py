from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from ..models import *

def message_presentation_get_redirect_url(message_presentation_element,session):
    if not message_presentation_element.final_element:
        return message_presentation_element.redirect.get_absolute_url(session)
    else:
        return None



def message_presentation_generate_context(message_presentation_element,session):
    language = session.language
    print('Language')
    print(language)
    print(message_presentation_element)
    print(session)
    message_voice_fragment_url = message_presentation_element.get_voice_fragment_url(language)
    print(message_voice_fragment_url)
    print('-----*****END*****-----')
    redirect_url = message_presentation_get_redirect_url(message_presentation_element,session)
    context = {'message_voice_fragment_url':message_voice_fragment_url,
            'redirect_url':redirect_url}
    return context


def message_presentation(request, element_id, session_id):
    print('-----*****MESSAGE*****-----')
    message_presentation_element = get_object_or_404(MessagePresentation, pk=element_id)
    session = get_object_or_404(CallSession, pk=session_id)
    session.record_step(message_presentation_element)
    context = message_presentation_generate_context(message_presentation_element, session)
    print(message_presentation_element)
    print(request)
    print(element_id)
    print(session_id)
    print(message_presentation_element)
    return render(request, 'message_presentation.xml', context, content_type='text/xml')

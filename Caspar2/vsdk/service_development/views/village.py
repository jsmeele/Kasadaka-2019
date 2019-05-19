from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect

from ..models import CallSession, VoiceService, Village

from . import base

# Create your views here.
class VillageSelection(TemplateView):

    def render_village_selection_form(self, request, session, redirect_url):
        villages = Village.objects.all()
        language = session.language
        labels = []

        print('-----*****VILLAGE*****-----')
        print(villages)
        for v in villages:
            labels.append(v.village.get_voice_fragment_url(language))
        # village_element = get_object_or_404(Village, pk=element_id)
        # print(village_element)
        print(language)

        # This is the redirect URL to POST the Village selected
        # redirect_url_POST = reverse('service-development:village-selection', args = [session.id])
        redirect_url_POST = reverse('service-development:village-selection', args =[session.id])
        # This is the redirect URL for *AFTER* the Village selection process
        pass_on_variables = {'redirect_url' : redirect_url}

        context = {'villages' : villages,
                   'labels' : labels,
                   'redirect_url' : redirect_url_POST,
                   'pass_on_variables' : pass_on_variables
                   }

        return render(request, 'village_selection.xml', context, content_type='text/xml')

    def get(self, request, session_id):
        """
        Asks the user to select one of the villages.
        """
        session = get_object_or_404(CallSession, pk = session_id)

        print('-----VILLAGE_GET-------')
        print(request.GET)
        print(session.language)

        voice_service = session.service
        # if 'redirect_url' in request.GET:
        #     redirect_url = request.GET['redirect_url']
        redirect_url = reverse('service-development:user-registration', args =[session.id])
        return self.render_village_selection_form(request, session, redirect_url)

    def post(self, request, session_id):
        """
        Saves the chosen village to the session
        """
        print('-----VILLAGE_POST-------')
        print(request.POST)
        if 'redirect_url' in request.POST:
            redirect_url = request.POST['redirect_url']

        else: raise ValueError('Incorrect request, redirect_url not set')
        if 'village_id' not in request.POST:
            raise ValueError('Incorrect request, village ID not set')

        session = get_object_or_404(CallSession, pk = session_id)
        voice_service = session.service
        village = get_object_or_404(Village, pk = request.POST['village_id'])

        session._village = village
        session.save()

        session.record_step(None, "Village selected, %s" % village.name)

        return HttpResponseRedirect(redirect_url)

    # def create_new_village(self, request, session):
    #     """
    #     After all required elements of the registration process
    #     have been filled, this function creates the village.
    #     After registration the village is redirected back to the start
    #     of the voice service.
    #     """
    #     name = session.name
    #     #register the village and link the session to the village
    #     village = Village(name = name, address = address)
    #     village.save()
    #     session.record_step(None, "Registered a village: %s" % str(village))
    #     return
    #
    # def village_registration_process(self, request, session):
    #     """
    #     This function redirects to the set elements of the user registration
    #     process, and redirects to the final registration when all elements have
    #     been filled.
    #     """
    #     # Always redirect back to registration process
    #     redirect_url = reverse('service-development:village-registration', args =[session.id])
    #
    #     #TODO: dit verder uitwerken, user bestaat natuurlijk nog niet dus daar kun je niet checken.
    #     #if 'name' in session.service.registration_elements and session.user.name_voice == None:
    #         # go to user name voice prompt
    #     #    pass
    #
    #     # If all required elements are present, finalize registration by creating a new user
    #     self.create_new_village(request, session)
    #
    #     # Return to start of voice service
    #     return redirect('service-development:voice-service', voice_service_id = session.service.id, session_id = session.id)
    #
    # def get(self, request, session_id):
    #     # print("TEST3")
    #     session = get_object_or_404(CallSession, pk = session_id)
    #     return self.village_registration_process(request, session)

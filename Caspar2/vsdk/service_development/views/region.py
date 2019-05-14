from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect

from ..models import CallSession, VoiceService, Region

# Create your views here.
class RegionSelection(TemplateView):

    def render_region_selection_form(self, request, session, redirect_url):
        regions = Region.objects.all()

        # This is the redirect URL to POST the Region selected
        # redirect_url_POST = reverse('service-development:village-selection', args = [session.id])
        redirect_url_POST = reverse('service-development:region-selection', args =[session.id])
        # This is the redirect URL for *AFTER* the Region selection process
        pass_on_variables = {'redirect_url' : redirect_url}

        context = {'regions' : regions,
                   'redirect_url' : redirect_url_POST,
                   'pass_on_variables' : pass_on_variables
                   }
        return render(request, 'region_selection.xml', context, content_type='text/xml')

    def get(self, request, session_id):
        """
        Asks the user to select one of the regions.
        """
        print('-----REGION_GET-------')
        print(request.GET)

        session = get_object_or_404(CallSession, pk = session_id)
        voice_service = session.service
        # if 'redirect_url' in request.GET:
        #     redirect_url = request.GET['redirect_url']
        redirect_url = reverse('service-development:user-registration', args =[session.id])
        # redirect_url = reverse('service-development:village-selection', args = [session.id])
        return self.render_region_selection_form(request, session, redirect_url)

    def post(self, request, session_id):
        """
        Saves the chosen region to the session
        """
        print('-----REGION_POST-------')
        print(request.POST)
        if 'redirect_url' in request.POST:
            redirect_url = request.POST['redirect_url']
        else: raise ValueError('Incorrect request, redirect_url not set')
        if 'region_id' not in request.POST:
            raise ValueError('Incorrect request, region ID not set')

        session = get_object_or_404(CallSession, pk = session_id)
        voice_service = session.service
        region = get_object_or_404(Region, pk = request.POST['region_id'])

        session._region = region
        session.save()

        session.record_step(None, "Region selected, %s" % region.name)

        return HttpResponseRedirect(redirect_url)


    # def create_new_region(self, request, session):
    #     """
    #     After all required elements of the registration process
    #     have been filled, this function creates the region.
    #     After registration the region is redirected back to the start
    #     of the voice service.
    #     """
    #     name = session.name
    #     #register the region and link the session to the region
    #     region = Region(name = name, address = address)
    #     region.save()
    #     session.record_step(None, "Registered a region: %s" % str(region))
    #     return
    #
    # def region_registration_process(self, request, session):
    #     """
    #     This function redirects to the set elements of the user registration
    #     process, and redirects to the final registration when all elements have
    #     been filled.
    #     """
    #     # Always redirect back to registration process
    #     redirect_url = reverse('service-development:region-selection', args =[session.id])
    #
    #     #TODO: dit verder uitwerken, user bestaat natuurlijk nog niet dus daar kun je niet checken.
    #     #if 'name' in session.service.registration_elements and session.user.name_voice == None:
    #         # go to user name voice prompt
    #     #    pass
    #
    #     # If all required elements are present, finalize registration by creating a new user
    #     self.create_new_region(request, session)
    #
    #     # Return to start of voice service
    #     return redirect('service-development:voice-service', voice_service_id = session.service.id, session_id = session.id)
    #
    # def get(self, request, session_id):
    #     # print("TEST3")
    #     session = get_object_or_404(CallSession, pk = session_id)
    #     return self.region_registration_process(request, session)

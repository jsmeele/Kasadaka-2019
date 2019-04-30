from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from ..models import region

from . import base

# Create your views here.
class RegionRegistration(TemplateView):

    def create_new_region(self, request, session):
        """
        After all required elements of the registration process
        have been filled, this function creates the region.
        After registration the region is redirected back to the start
        of the voice service.
        """
        name = session.name
        #register the region and link the session to the region
        region = Region(name = name, address = address)
        region.save()
        session.record_step(None, "Registered a region: %s" % str(region))
        return

    def region_registration_process(self, request, session):
        """
        This function redirects to the set elements of the user registration
        process, and redirects to the final registration when all elements have
        been filled.
        """
        # Always redirect back to registration process
        redirect_url = reverse('service-development:region-registration', args =[session.id])

        #TODO: dit verder uitwerken, user bestaat natuurlijk nog niet dus daar kun je niet checken.
        #if 'name' in session.service.registration_elements and session.user.name_voice == None:
            # go to user name voice prompt
        #    pass

        # If all required elements are present, finalize registration by creating a new user
        self.create_new_region(request, session)

        # Return to start of voice service
        return redirect('service-development:voice-service', voice_service_id = session.service.id, session_id = session.id)

    def get(self, request, session_id):
        # print("TEST3")
        session = get_object_or_404(CallSession, pk = session_id)
        return self.region_registration_process(request, session)

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate

from selvbetjening.core.invoice.decorators import disable_invoice_updates
from selvbetjening.core.events.models import attendes_event_source
from selvbetjening.core.events.decorators import \
     event_registration_open_required, \
     event_registration_allowed_required, \
     get_event_from_id

from selvbetjening.portal.eventregistration.forms import OptionForms

from forms import SignupSubmitForm, InlineRegistrationForm

@get_event_from_id
@event_registration_open_required
@event_registration_allowed_required
@disable_invoice_updates
def registration(request, event,
                 form_options=OptionForms,
                 form_user=InlineRegistrationForm,
                 signupsubmit_form=SignupSubmitForm,
                 template='simpleregistration/registration.html',
                 success_view='avacon_invoice'):

    if request.method == 'POST':
        optionforms = form_options(event, request.POST)
        userform = form_user(request.POST)
        signupsubmitform = signupsubmit_form(request.POST)

        if optionforms.is_valid() and userform.is_valid() and \
           signupsubmitform.is_valid():

            user = userform.save()
            attendee = event.add_attendee(user)
            optionforms.save(attendee=attendee)

            attendee.invoice.update(force=True)

            attendes_event_source.trigger(user, attendee=attendee)

            user_obj = authenticate(username=user.username,
                                    password=userform.cleaned_data['password1'])
            login(request, user_obj)

            return HttpResponseRedirect(reverse(success_view))
    else:
        optionforms = form_options(event)
        userform = form_user()
        signupsubmitform = signupsubmit_form()

    return render(request, template,
                  {'event' : event,
                   'userform' : userform,
                   'optionforms' : optionforms,
                   'signupsubmitform' : signupsubmitform})

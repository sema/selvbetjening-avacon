
from django.utils.translation import ugettext_lazy as _
from django import forms

from uni_form.helpers import FormHelper, Submit, Layout

from selvbetjening.viewbase.forms.helpers import InlineFieldset
from selvbetjening.portal.eventregistration.forms import AcceptForm
from selvbetjening.core.members.forms import RegistrationForm

class SignupSubmitForm(forms.Form):
    helper = FormHelper()
    helper.add_layout(Layout(InlineFieldset(None)))
    helper.form_tag = False
    helper.add_input(Submit('submit_signupsubmitform', _('Register for event')))

class InlineRegistrationForm(RegistrationForm):
    def __init__(self, *args, **kwargs):
        super(InlineRegistrationForm, self).__init__(*args, **kwargs)
        self.helper.inputs = []
        self.helper.form_tag = False
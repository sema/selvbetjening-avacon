
from django.utils.translation import ugettext_lazy as _
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

from selvbetjening.core.members.forms import RegistrationForm


class SignupSubmitForm(forms.Form):
    helper = FormHelper()
    helper.add_layout(Layout())
    helper.form_tag = False
    helper.add_input(Submit('submit_signupsubmitform', _('Register for event')))


class InlineRegistrationForm(RegistrationForm):
    def __init__(self, *args, **kwargs):
        super(InlineRegistrationForm, self).__init__(*args, **kwargs)
        self.helper.inputs = []
        self.helper.form_tag = False
from datetime import timedelta, date

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings

from selvbetjening.core.events.tests import Database as EventDatabase
from selvbetjening.core.events.forms import OptionGroupForm

import forms
from mailer.models import Message

class Fixtures(object):
    valid_registration = {
            'name' : 'John Doe',
            'dateofbirth' : '1987-10-14',
            'email' : 'example@example.org',
            'street' : 'duck street',
            'postalcode' : '1000',
            'city' : 'duck town',
            'country': 'DK',
        }

class RegistrationTest(TestCase):
    def setUp(self):
        self.event = EventDatabase.new_event()

    def test_successfull_registration(self):
        resp = self.client.post(reverse('avacon_registration'), Fixtures.valid_registration, follow=True)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.event.attendees_count, 1)

class SvsProfileFormTest(TestCase):
    def test_valid_registration(self):
        form = forms.SvsProfileForm(Fixtures.valid_registration)
        print form.errors
        self.assertTrue(form.is_valid())

class SvsEmailRegistrationTest(TestCase):
    def setUp(self):
        self.event = EventDatabase.new_event()

    def test_registration_gopher_email(self):
        optiongroup = EventDatabase.new_optiongroup(self.event)
        option = EventDatabase.new_option(optiongroup, id=settings.GOPHER_EMAIL_OPTION)

        post_data = Fixtures.valid_registration.copy()
        post_data[OptionGroupForm._get_id(option)] = 'true'

        resp = self.client.post(reverse('avacon_registration'), post_data, follow=True)

        self.assertEqual(resp.status_code, 200)

        messages = Message.objects.all()

        self.assertEqual(len(messages), 2)

    def test_registration_cosplay_email(self):
        optiongroup1 = EventDatabase.new_optiongroup(self.event)
        option1 = EventDatabase.new_option(optiongroup1, id=settings.COSPLAY_EMAIL_OPTIONS[0])

        optiongroup2 = EventDatabase.new_optiongroup(self.event)
        option2 = EventDatabase.new_option(optiongroup2, id=settings.COSPLAY_EMAIL_OPTIONS[1])

        post_data = Fixtures.valid_registration.copy()
        post_data[OptionGroupForm._get_id(option1)] = 'true'
        post_data[OptionGroupForm._get_id(option2)] = 'true'

        resp = self.client.post(reverse('avacon_registration'), post_data, follow=True)

        self.assertEqual(resp.status_code, 200)

        messages = Message.objects.all()

        self.assertEqual(len(messages), 2)
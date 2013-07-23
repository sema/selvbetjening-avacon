"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from datetime import date

from decimal import Decimal

from django.test import TestCase

from selvbetjening.core.events.tests import Database
from selvbetjening.core.invoice.models import Invoice

import models

#class TestPriceModel(TestCase):
    #def test_early_access_price(self):
        #event = Database.new_event()
        #user = Database.new_user()

        #attendee = event.add_attendee(user)

        #eventrate = SvsEventRates.objects.create(selected_rate='earlyaccess', attendee=attendee)

        #self.assertEqual(eventrate.price, 250)

    #def test_normal_price(self):
        #event = Database.new_event()
        #user = Database.new_user()

        #attendee = event.add_attendee(user)

        #eventrate = SvsEventRates.objects.create(selected_rate='normal', attendee=attendee)

        #self.assertEqual(eventrate.price, 300)

    #def test_added_to_invoices(self):
        #event = Database.new_event()
        #user = Database.new_user()

        #attendee = event.add_attendee(user)

        #eventrate = SvsEventRates.objects.get(attendee=attendee)

        #self.assertTrue(attendee.invoice.total_price > 0)

    #def test_removed_on_attendee_delete(self):
        #event = Database.new_event()
        #user = Database.new_user()

        #attendee = event.add_attendee(user)
        #invoice_id = int(attendee.invoice.pk)

        #self.assertTrue(attendee.invoice.total_price > 0)

        #attendee.delete()

        #invoice = Invoice.objects.get(pk=invoice_id)

        #self.assertEqual(invoice.total_price, 0)

    #def test_added_rate_by_date_future(self):
        #event = Database.new_event()
        #user = Database.new_user()

        #class DateStub(object):
            #@staticmethod
            #def today():
                #return date(2012, 5, 1)

        #models.datetime.date = DateStub
        #attendee = event.add_attendee(user)
        #models.datetime.date = date

        #self.assertEqual(attendee.invoice.total_price, Decimal(300))

    #def test_added_rate_by_date(self):
        #event = Database.new_event()
        #user = Database.new_user()

        #class DateStub(object):
            #@staticmethod
            #def today():
                #return date(2009, 5, 1)

        #models.datetime.date = DateStub
        #attendee = event.add_attendee(user)
        #models.datetime.date = date

        #self.assertEqual(attendee.invoice.total_price, Decimal(250))










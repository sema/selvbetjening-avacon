import datetime

from django.db import models
from django.db.models.signals import post_save, post_delete

from selvbetjening.core.events.models import Attend
from selvbetjening.core.invoice.signals import populate_invoice



#def add_attendee_handler(sender, **kwargs):
    #created = kwargs.get('created')
    #instance = kwargs.get('instance')

    #if created and not instance.user.has_perm('eventprice.exempt_from_payment'):
        #if datetime.date.today() < RATE_CHANGE_DATE:
            #SvsEventRates.objects.create(selected_rate='earlyaccess', attendee=instance)
        #else:
            #SvsEventRates.objects.create(selected_rate='normal', attendee=instance)

        #instance.invoice.update()

#post_save.connect(add_attendee_handler, sender=Attend)

#def update_invoice_with_event_rates(sender, **kwargs):
    #invoice_revision = kwargs['invoice_revision']
    #invoice = invoice_revision.invoice

    #for eventrate in SvsEventRates.objects.filter(attendee__invoice=invoice):
        #invoice_revision.add_line(description=unicode(eventrate),
                                  #price=eventrate.price,
                                  #managed=True)

#populate_invoice.connect(update_invoice_with_event_rates)


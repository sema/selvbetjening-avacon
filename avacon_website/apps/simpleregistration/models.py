
from selvbetjening.core.events.models import request_attendee_pks_signal, find_attendee_signal, Attend


def avacon_style_attendee_pks_handler(sender, **kwargs):
    attendee = kwargs['attendee']
    key = 'Avacon.%s.%s.%s' % (attendee.event.pk,
                               attendee.user.pk,
                               attendee.invoice.pk)

    return ('Avacon-Style ID', key)

request_attendee_pks_signal.connect(avacon_style_attendee_pks_handler)


def avacon_style_find_attendee_handler(sender, **kwargs):
    pk = kwargs['pk']

    try:
        avacon, event_pk, user_pk, invoice_pk = pk.split('.')

        attendee = Attend.objects.get(user__pk=user_pk,
            invoice__pk=invoice_pk,
            event__pk=event_pk)

        return ('Avacon', attendee)

    except:
        return None

find_attendee_signal.connect(avacon_style_find_attendee_handler)
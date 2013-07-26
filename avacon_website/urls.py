from django.conf.urls import *

from selvbetjening.sadmin.base import sadmin

from selvbetjening.sadmin.members.models import MembersRootAdmin
from selvbetjening.sadmin.events.models import EventsRootAdmin
from selvbetjening.sadmin.mailcenter.models import MailcenterRootAdmin

sadmin.site.register('members', MembersRootAdmin)
sadmin.site.register('events', EventsRootAdmin)
sadmin.site.register('mailcenter', MailcenterRootAdmin)

urlpatterns = patterns('',
    (r'^sadmin/', include(sadmin.site.urls)),

    (r'^', include('avacon_website.apps.simpleregistration.urls')),
)

#sadmin.main_menu.register(DirectPage('Avacon 2012',
#                                     'http://tilmelding.avacon.dk/sadmin/events/3/attendees/'))


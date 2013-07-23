from django.conf.urls.defaults import *
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from selvbetjening.sadmin.base import sadmin
from selvbetjening.sadmin.base.nav import DirectPage, RemoteSPage

# workaround for missing urls
from selvbetjening.sadmin.members import models as members_models
from selvbetjening.sadmin.events import models as event_models
from selvbetjening.sadmin.mailcenter import models as mail_models

urlpatterns = patterns('',
    (r'^sadmin/', include(sadmin.site.urls)),

    (r'^', include('avacon_website.apps.simpleregistration.urls')),
)

#sadmin.main_menu.register(DirectPage('Avacon 2012',
#                                     'http://tilmelding.avacon.dk/sadmin/events/3/attendees/'))


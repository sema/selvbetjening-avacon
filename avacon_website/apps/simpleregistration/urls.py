from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views
from django.conf import settings

from selvbetjening.portal.profile.forms import LoginForm
from selvbetjening.portal.eventregistration import views as eventregistration_views

import views

urlpatterns = patterns('',

    url(r'^min-oversigt/log-ud/$', auth_views.logout,
        {'template_name': 'profile/logout.html',},
        name='members_logout'),

    url(r'^min-oversigt/tilvalg/$',
        eventregistration_views.change_options,
        kwargs={'event_id': settings.AVACON_EVENT_ID,
                'success_page': 'avacon_invoice',
                'omit_event_id_on_success': True,
                'template_name': 'simpleregistration/change_options.html'},
        name='avacon_tilvalg'),

    url(r'^min-oversigt/$',
        eventregistration_views.view_invoice,
        kwargs={'event_id': settings.AVACON_EVENT_ID,
                'template_name': 'simpleregistration/status.html'},
        name='avacon_invoice'),

    url(r'^ny-tilmelding/$',
        views.registration,
        name='avacon_registration',
        kwargs={'event_id': settings.AVACON_EVENT_ID}),

    url(r'^nulstil-kodeord/$', auth_views.password_reset,
        {'template_name':'profile/password_reset/password_reset.html',
         'email_template_name':'simpleregistration/password_reset_email.html'}, name='auth_password_reset'),
    url(r'^nulstil-kodeord/email-sendt/$', auth_views.password_reset_done,
        {'template_name':'profile/password_reset/password_reset_done.html'},
        name='members_password_reset_done'),
    url(r'^nulstil-kodeord/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/', auth_views.password_reset_confirm,
        {'template_name':'profile/password_reset/password_reset_confirm.html'},
        name='auth_password_reset_confirm'),
    url(r'^nulstil-kodeord/reset/done/$', auth_views.password_reset_complete,
        {'template_name':'simpleregistration/password_reset_done.html'}),

    url(r'^$',
        auth_views.login,
        {'template_name': 'simpleregistration/index.html',
         'authentication_form': LoginForm},
        name='avacon_index'),
)

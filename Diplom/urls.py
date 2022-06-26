"""
Definition of urls for Diplom.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^zaglushka$', app.views.zaglushka, name='zaglushka'),
    url(r'^foreign_profile/(?P<id>\d+)/$', app.views.foreign_profile, name='foreign_profile'),
    url(r'^users/$', app.views.users, name='users'),
   	url(r'^inbox/$', app.views.Inbox, name='inbox'),
   	url(r'^directs/(?P<username>\w{0,50})/$', app.views.Directs, name='directs'),
   	url(r'^search/$', app.views.UserSearch, name='usersearch'),
   	url(r'^new/(?P<username>\w{0,50})/$', app.views.NewConversation, name='newconversation'),
   	url(r'^send/$', app.views.SendDirect, name='send_direct'),
    url(r'^profile$', app.views.profile, name='profile'),
    url(r'^registration$', app.views.registration, name='registration'),
    url(r'^edit-profile$', app.views.editUser, name='edit-profile'),
    url(r'^edit-photo$', app.views.editPhoto, name='edit-photo'),
    url(r'^news/$', app.views.news, name='news'),
    url(r'^tasks/$', app.views.tasks, name='tasks'),
    url(r'^news/(?P<parametr>\d+)/$', app.views.newspost, name='newspost'),
    url(r'newpost', app.views.newpost, name='newpost'),
    url(r'newtask', app.views.newtask, name='newtask'),
    url(r'^ConfirmTask(?P<parametr>\d+)/$', app.views.ConfirmTask, name='ConfirmTask'),
    url(r'^RejectTask(?P<parametr>\d+)/$', app.views.RejectTask, name='RejectTask'),
    url(r'^DeleteTask(?P<parametr>\d+)/$', app.views.DeleteTask, name='DeleteTask'),
    url(r'^ResetTask(?P<parametr>\d+)/$', app.views.ResetTask, name='ResetTask'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Вход',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
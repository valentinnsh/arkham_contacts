from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^expansions/$', views.ExpansionsListView.as_view(), name='expansions'),
    url(r'^expansions/(?P<pk>\d+)/$', views.ExpansionsDetailView.as_view(), name='expansions_detail'),
    url(r'^contacts/(?P<pk>\d+)/$', views.ContactsDetailView.as_view(), name='contacts_detail'),   
    url(r'^locations/(?P<pk>\d+)/$', views.LocationsDetailView.as_view(), name='locations_detail')
]

urlpatterns += [
    url(r'^expansions/create/$', views.ExpansionsCreate.as_view(), name='expansions_create'),
    url(r'^expansions/(?P<pk>\d+)/update/$', views.ExpansionsUpdate.as_view(), name='expansions_update'),
    url(r'^expansions/(?P<pk>\d+)/delete/$', views.ExpansionsDelete.as_view(), name='expansions_delete'),
]

urlpatterns += [
    url(r'^locations/create/$', views.LocationsCreate.as_view(), name='locations_create'),
    url(r'^locations/(?P<pk>\d+)/update/$', views.LocationsUpdate.as_view(), name='locations_update'),
    url(r'^locations/(?P<pk>\d+)/delete/$', views.LocationsDelete.as_view(), name='locations_delete'),
]

urlpatterns += [
    url(r'^contacts/create/$', views.ContactsCreate.as_view(), name='contacts_create'),
    url(r'^contacts/(?P<pk>\d+)/update/$', views.ContactsUpdate.as_view(), name='contacts_update'),
    url(r'^contacts/(?P<pk>\d+)/delete/$', views.ContactsDelete.as_view(), name='contacts_delete'),
]

urlpatterns += [
    url(r'^giverandomcontact/$', views.GiveRandomContact, name = 'random_contact'),
]

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    
    # Filtering and info
    url(r'^filter/$', views.FilterStartups.as_view(), name="filter_startups"),
    url(r'^filter/save/$', views.filter_save, name="filter_save"),
    url(r'^discover/$', views.discover_startups, name="discover_startups"),
    url(r'^startups/(?P<pk>[0-9]+)/$', views.StartupDetail.as_view(), name="startup_detail"),
    
    # Notes
    url(r'^notes/(?P<pk>[0-9]+)/delete/$', views.note_delete, name="note_delete"),
    
    # My startups info
    url(r'^startups/$', views.my_startups, name="my_startups"),
    url(r'^add/(?P<pk>[0-9]+)/$', views.add_startup, name="startup_add"),
    url(r'^remove/(?P<pk>[0-9]+)/$', views.remove_startup, name="startup_remove"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.hide_startup, name="startup_delete"),
    
    # Collections
    url(r'^collections/$', views.my_collections, name="my_collections"),
    url(r'^collections/(?P<pk>[0-9]+)/$', views.collection_detail, name="collection_detail"),
    url(r'^collections/new/$', views.new_collection, name="new_collection"),
    url(r'^collections/(?P<pk>[0-9]+)/delete/$', views.collection_delete, name="collection_delete"),
    
    # Account actions
    url(r'^login/$', views.login, name="login"),
    url(r'logout/$', views.logout, name="logout"),
]
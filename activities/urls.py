from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^activities/$', views.activity_list, name='activities'),
    url(r'^activities/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
    url(r'^activities/new/$', views.activity_new, name='activity_new'),
    url(r'^activities/(?P<pk>\d+)/edit/$', views.activity_edit, name='activity_edit'),

    url(r'^shoes/$', views.shoe_list, name='shoes'),
    url(r'^shoes/(?P<pk>\d+)/$', views.shoe_detail, name='shoe_detail'),
    url(r'^shoes/new/$', views.shoe_new, name='shoe_new'),
    url(r'^shoes/(?P<pk>\d+)/edit/$', views.shoe_edit, name='shoe_edit'),

    url(r'^bikes/$', views.bike_list, name='bikes'),
    url(r'^bikes/(?P<pk>\d+)/$', views.bike_detail, name='bike_detail'),
    url(r'^bikes/new/$', views.bike_new, name='bike_new'),
    url(r'^bikes/(?P<pk>\d+)/edit/$', views.bike_edit, name='bike_edit'),
]

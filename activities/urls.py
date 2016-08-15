from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^activity/$', views.activity_list, name='activities'),
    url(r'^activity/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
    url(r'^activity/new/$', views.new_activity, name='new_activity'),
    url(r'^activity/(?P<pk>\d+)/edit/$', views.edit_activity, name='edit_activity'),

    url(r'^shoe/$', views.shoe_list, name='shoes'),
    url(r'^shoe/(?P<pk>\d+)/$', views.shoe_detail, name='shoe_detail'),
    url(r'^shoe/new/$', views.new_shoe, name='new_shoe'),
    url(r'^shoe/(?P<pk>\d+)/edit/$', views.edit_shoe, name='edit_shoe'),

    url(r'^bike/$', views.bike_list, name='bikes'),
    url(r'^bike/(?P<pk>\d+)/$', views.bike_detail, name='bike_detail'),
    url(r'^bike/new/$', views.new_bike, name='new_bike'),
    url(r'^bike/(?P<pk>\d+)/edit/$', views.edit_bike, name='edit_bike'),
]

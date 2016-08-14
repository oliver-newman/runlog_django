from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.activity_list, name='activities'),
    url(r'^activity/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
    url(r'^activity/new/$', views.new_activity, name='new_activity'),
    url(r'^activity/(?P<pk>\d+)/edit/$', views.edit_activity, name='edit_activity'),
    url(r'^shoe/new/$', views.new_shoe, name='new_shoe'),
    url(r'^bike/new/$', views.new_bike, name='new_bike'),
]

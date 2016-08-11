from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.activity_list, name='activities'),
    url(r'^new', views.index, name='index'),
]

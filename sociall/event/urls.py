from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('new_event', views.new_event, name='new_event'),
    url('create_event', views.create_event, name='create_event'),
    url(r'^(?P<event_id>[0-9]+)/$', views.show, name='show'),
    url(r'^(?P<event_id>[0-9]+)/delete$', views.delete_event, name='delete_event'),

]
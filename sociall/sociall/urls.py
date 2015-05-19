from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sociall.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^event/', include('event.urls', namespace="event")),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^admin/', include(admin.site.urls)),
]

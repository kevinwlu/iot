from django.conf.urls import include, url
from django.contrib import admin
from myapp import views
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

# Django URL patterns for REST services and
# home intrusion detection application - urls.py

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from myapp import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'room', views.RoomViewSet)
router.register(r'door', views.DoorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home),
]

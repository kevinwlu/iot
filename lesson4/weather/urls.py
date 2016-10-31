from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from myapp import views
admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'dt', views.DtViewSet)
router.register(r'tmp', views.TmpViewSet)
router.register(r'hmd', views.HmdViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home),
]

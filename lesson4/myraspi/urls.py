from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from rest_framework import routers
from myapp import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register('dt', views.DtViewSet)
router.register('tmp', views.TmpViewSet)
router.register('cpu', views.CpuViewSet)

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(
                        url=staticfiles_storage.url('favicon.ico'),
                        permanent=False), name="favicon"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('home/', views.home),
]

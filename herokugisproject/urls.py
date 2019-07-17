from django.urls import path,include
from django.contrib import admin
from drfapp.views import UserViewSet, GroupViewSet, ConstituencyViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'constituencies', ConstituencyViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += [
    path('', include(router.urls))
]
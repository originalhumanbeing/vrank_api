from django.conf.urls import url, include
from .views import VarietyShowViewSet, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'all', VarietyShowViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]

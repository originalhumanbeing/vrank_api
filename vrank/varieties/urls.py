from django.conf.urls import url, include
from .views import VarietyShowViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'all', VarietyShowViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]

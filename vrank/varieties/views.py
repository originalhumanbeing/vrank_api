from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import VarietyShow
from .serializers import UserSerializer, VarietyShowSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class VarietyShowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = VarietyShow.objects.all()
    serializer_class = VarietyShowSerializer




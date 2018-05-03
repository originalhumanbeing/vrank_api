from rest_framework import viewsets

from .models import VarietyShow
from .serializers import VarietyShowSerializer


class VarietyShowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = VarietyShow.objects.all()
    serializer_class = VarietyShowSerializer




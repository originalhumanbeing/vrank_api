from django.contrib.auth.models import User
from .models import VarietyShow
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class VarietyShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VarietyShow
        fields = ('title', 'desc', 'created_date', 'last_modified_date', 'air_time', 'air_day', 'broadcasting_station')

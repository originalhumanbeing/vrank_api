from django.db import models
from django.utils import timezone


class VarietyShow(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    last_modified_date = models.DateTimeField()
    air_time = models.CharField(max_length=10)
    air_day = models.CharField(max_length=5)
    broadcasting_station = models.CharField(max_length=10)

    def __str__(self):
        return self.title


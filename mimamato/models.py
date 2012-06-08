from django.db import models

# Create your models here.

class MediaUrl(models.Model):

    url = models.URLField()
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    description = models.TextField(blank=True, null=True)

    TYPE_WEBCAM = 0
    TYPE_WEATHERFORECAST = 1
    TYPE_WEATHERDATA = 2
    TYPE_PICTURE = 3
    TYPE_INACTIVE = 3

    TYPE_CHOICES = (
        (TYPE_WEBCAM, 'webcam'),
        (TYPE_WEATHERFORECAST, 'weather forecast'),
        (TYPE_WEATHERDATA, 'weather data'),
        (TYPE_PICTURE, 'pic'),
        (TYPE_INACTIVE, 'inactive'),
    )

    type = models.PositiveIntegerField(choices=TYPE_CHOICES)

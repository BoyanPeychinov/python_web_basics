from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
    )
    last_name = models.CharField(
        max_length=20,
    )
    age = models.IntegerField()
    image_url = models.URLField()

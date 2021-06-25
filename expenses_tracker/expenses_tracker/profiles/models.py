from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
    )
    last_name = models.CharField(
        max_length=15,
    )
    budget = models.IntegerField()

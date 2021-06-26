from django.db import models

from petstagram_2.pets.models import Pet


class Comment(models.Model):
    text = models.TextField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

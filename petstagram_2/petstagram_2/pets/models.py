from django.db import models


class Pet(models.Model):
    CAT_CHOICE = 'cat'
    DOG_CHOICE = 'dog'
    PARROT_CHOICE = 'parrot'
    POSSIBLE_CHOICES = [
        ('cat', CAT_CHOICE),
        ('dog', DOG_CHOICE),
        ('parrot', PARROT_CHOICE),
    ]

    type = models.CharField(
        max_length=6,
        choices=POSSIBLE_CHOICES,
    )
    name = models.CharField(
        max_length=6,
    )
    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField()


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
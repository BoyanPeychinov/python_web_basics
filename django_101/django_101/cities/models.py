from django.db.models import Model, CharField, IntegerField


class Person(Model):
    name = CharField(max_length=30)
    age = IntegerField()
    home_town = CharField(max_length=25)
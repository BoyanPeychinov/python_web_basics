from django.http import HttpResponse
from django.shortcuts import render

from django_101.cities.models import Person


def index(req):
    context = {
        "name": "Boyan",
        "people": Person.objects.all()
    }

    return render(req, "index.html", context)


def list_phones(req):
    return HttpResponse('Phones list')

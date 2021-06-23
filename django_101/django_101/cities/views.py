from django.http import HttpResponse
from django.shortcuts import render

from django_101.cities.models import Person


def show_forms_demo(req):
    return render(req, 'forms_demo.html')


def index(req):
    context = {
        "name": "Boyan",
        "people": Person.objects.all()
    }

    return render(req, "index.html", context)


def list_phones(req):
    context = {'phones': [
        {
            "name": 'Galaxy S5000',
            'quantity': 3,
        },
        {
            'name': 'Xiaomi Readmi T9',
            'quantity': 0,
        },
        {
            'name': 'iPhone 12',
            'quantity': 4,
        }
    ], 'message': "Phones list"}

    return render(req, 'phones.html', context)

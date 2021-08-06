from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = 'landing_page.html'


# def landing_page(req):
#     return render(req, 'landing_page.html')


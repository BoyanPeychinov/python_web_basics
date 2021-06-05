from django.urls import path

from urls_and_templates.secondary_app import views

urlpatterns = [
    path('', views.index),
]
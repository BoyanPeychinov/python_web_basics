from django.urls import path

from urls_and_templates.main_app import views

urlpatterns = [
    path('', views.index),
]
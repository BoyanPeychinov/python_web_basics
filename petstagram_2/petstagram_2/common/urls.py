from django.urls import path

from petstagram_2.common.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing page')
]
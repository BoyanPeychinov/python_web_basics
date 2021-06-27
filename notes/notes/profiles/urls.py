from django.urls import path

from notes.profiles.views import show_profile, create_profile, delete_profile

urlpatterns = [
    path('', show_profile, name='show profile'),
    path('create/', create_profile, name='create profile'),
    # path('edit/<int:pk>', edit_profile, 'edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]
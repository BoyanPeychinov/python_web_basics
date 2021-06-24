from django.urls import path

from petstagram.pets.views import list_pets, pet_details, like_pet, create_pet, update_pet, delete_pet, comment_pet

urlpatterns = [
    path('', list_pets, name='list pets'),
    path('details/<int:pk>', pet_details, name='pet details'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('create/', create_pet, name='create pet'),
    path('edit/<int:pk>', update_pet, name='update pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
    path('comment/<int:pk>', comment_pet, name='comment pet'),
]
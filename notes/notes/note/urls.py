from django.urls import path

from notes.note.views import create_note, edit_note, delete_note, home, show_note_details

urlpatterns = [
    path('', home, name='home page'),
    path('add/', create_note, name='create note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', show_note_details, name='note details'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.note.urls')),
    path('profile/', include('notes.profiles.urls')),
]

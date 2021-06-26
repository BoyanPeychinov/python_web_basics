from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram_2.common.urls')),
    path('pets/', include('petstagram_2.pets.urls'))
]

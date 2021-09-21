from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('sex/', include('sex.urls')),
    path('', include('raselacademy.urls')),
    path('admin/', admin.site.urls),
]


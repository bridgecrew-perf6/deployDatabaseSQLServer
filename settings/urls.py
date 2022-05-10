from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from apps.connectionSQL import urls as u

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(u))
]

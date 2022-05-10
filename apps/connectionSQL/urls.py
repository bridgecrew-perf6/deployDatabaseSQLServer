from django.urls import path
from apps.connectionSQL import views as v

urlpatterns = [
    path('', v.home),

]

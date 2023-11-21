from django.urls import path
from .views import home
from .apps import HomeConfig


app_name = HomeConfig.name

urlpatterns = [
    path('', home, name='home'),
]
from django.urls import path
from .views import Information
from .apps import InformationConfig


app_name = InformationConfig.name

urlpatterns = [
    path('', Information.as_view(), name='information'),
]
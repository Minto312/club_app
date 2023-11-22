from django.urls import path
from .views import Information, information_data
from .apps import InformationConfig


app_name = InformationConfig.name

urlpatterns = [
    path('', Information.as_view(), name='information'),
    path('data/', information_data, name='information_data'),
]
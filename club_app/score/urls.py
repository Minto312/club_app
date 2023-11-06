from django.urls import path
from .views import Score, Recording
from .apps import ScoreConfig


app_name = ScoreConfig.name

urlpatterns = [
    path('', Score.as_view(), name='score'),
    path('recording', Recording.as_view(), name='recording'),
]
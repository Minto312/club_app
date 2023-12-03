from django.urls import path

#from club_app import score
from .views import Score, Recording, exam_chart, exam_data, exam_label
from .apps import ScoreConfig


app_name = ScoreConfig.name

urlpatterns = [
    path('', Score.as_view(), name='score'),
    path('exam_label', exam_label.as_view(), name='exam_label'),
    path('exam_data/<str:exam_name>', exam_data.as_view(), name='exam_data'),
    path('exam_chart/<str:exam_name>', exam_chart.as_view(), name='exam_chart'),
    path('recording', Recording.as_view(), name='recording'),
]
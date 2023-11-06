from django.urls import path
from .views import Attendance, data, qr
from .apps import AttendanceConfig


app_name = AttendanceConfig.name

urlpatterns = [
    path('', Attendance.as_view(), name='attendance'),
    path('data/',data,name='attendance_data'),
    path('qr/',qr,name='qr'),
]
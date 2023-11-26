from django.urls import path
from .views import Attendance, Activity, attendance_data, attend, register, activity_data
from .apps import AttendanceConfig

app_name = AttendanceConfig.name

urlpatterns = [
    path('', Attendance.as_view(), name='attendance'),
    path('attendance_data/<int:year>/<int:month>/', attendance_data, name='attendance_data'),
    path('attend/', attend, name='attend'),
    path('activity/', Activity.as_view(), name='activity'),
    path('activity/activity_data/<int:year>/<int:month>/', activity_data, name='activity_data'),
    path('register/', register, name='register'),   
]
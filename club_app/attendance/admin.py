from django.contrib import admin
from .models import AttendanceDB, ScheduleDB
# Register your models here.
admin.site.register(AttendanceDB)
admin.site.register(ScheduleDB)
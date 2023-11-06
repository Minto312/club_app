from django.contrib import admin
from .models import ExamDB, ScoreDB

# Register your models here.

admin.site.register(ExamDB)
admin.site.register(ScoreDB)
from django.db import models
from django.contrib.auth.models import User

class ScheduleDB(models.Model):
    ID = models.AutoField(primary_key=True) 
    date = models.DateTimeField()
    has_club_activity = models.BooleanField(default=False) 
    
    def __str__(self):
        return f'{self.date} : {self.has_club_activity}'

from django.db import models

# Create your models here.
class AttendanceDB(models.Model):
    ID = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} : {self.date}'

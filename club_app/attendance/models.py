from django.db import models

# Create your models here.
class AttendanceDB(models.Model):
    ID = models.AutoField(verbose_name='ID', primary_key=True) 
    name = models.CharField(verbose_name='ユーザー名', max_length=100)
    date = models.DateTimeField(verbose_name='日付', )
    attended = models.BooleanField(verbose_name='出席状況', )

    def __str__(self):
        return f'{self.name} : {self.date}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'date'],
                name="attend_unique"
            ),
        ]

class ScheduleDB(models.Model):
    ID = models.AutoField(verbose_name='ID', primary_key=True) 
    year = models.IntegerField(verbose_name='年')
    month = models.IntegerField(verbose_name='月')
    days = models.CharField(verbose_name='活動日', max_length=100)
    
    def __str__(self):
        return f'{self.year}-{self.month}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['year', 'month'],
                name="schedule_unique"
            ),
        ]

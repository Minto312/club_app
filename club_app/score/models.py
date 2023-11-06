from django.db import models
from django.contrib.auth import get_user_model
import uuid
import datetime

# Create your models here.

class ExamDB(models.Model):

    exam_name = models.CharField(max_length=100)

    def __str__(self):
        return self.exam_name


User = get_user_model()

class ScoreDB(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_id',
        verbose_name='ユーザー'
    )
    exam_name = models.ForeignKey(
        ExamDB,
        on_delete=models.CASCADE,
        related_name='exam_id',
        verbose_name='試験名'
    )
    score = models.IntegerField(verbose_name='点数')

    date = models.DateField(default=datetime.date.today,verbose_name='日付')


    def __str__(self):
        return f'{self.user.username}-{self.exam_name}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'exam_name'], name='unique_exam')
        ]
import uuid
from django.db import models
from django.utils import timezone

class Message_table(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #message
    text_message = models.TextField(blank=True, default=None)
    image_message = models.ImageField(upload_to='message/image_message/', default=None)
    file_message = models.FileField(upload_to='message/file_message/', default=None)
    #send_date
    send_date = models.DateTimeField(default=timezone.now)
    

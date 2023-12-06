import logging
from venv import logger
from django.shortcuts import render, redirect
from django.views import View
from .models import Message_table

logger = logging.getLogger(__name__)

import pytz
jst = pytz.timezone('Asia/Tokyo')

class Information(View):

    def get(self,request):
        logger.info(f'User {request.user.username} accessed information')
        messages_id = Message_table.objects.order_by('send_date').reverse().values('message_id')
        message_context_list = []
        
        for message_id in messages_id:
            message = Message_table.objects.get(message_id=message_id['message_id'])
            message_context = [f'<div id="message-id-{str(message_id)}" class="message"><p>{str(message.send_date.astimezone(jst).strftime('%Y-%m-%d %H:%M'))}</p>']

            if message.text_message :
                message_context.append(f'<div class="text-message"><p>{message.text_message}</p></div>')
            if message.image_message :
                message_context.append(f'<div class="image-message"><img src="/media/{message.image_message}"></div>')
            if message.file_message :
                message_context.append(f'<div class="file-message"><a href="/media/{message.file_message}" download="{message.file_message.name}">{message.file_message.name}</a></div>')
            message_context.append('</div>')
            message_context_list.append(''.join(message_context))

        context = {'messages':message_context_list}

        return render(request,'information/information.html', context)

    def post(self,request):
        logger.info(f'User {request.user.username} posted message')
        text_message = request.POST['text-message']
        image_message = request.FILES.get('image-message', None)
        file_message = request.FILES.get('file-message', None)
        Message_table.objects.create(text_message=text_message, image_message=image_message, file_message=file_message)
        logger.debug(f'User {request.user.username} posted message {text_message} {image_message} {file_message}')
        return redirect('http://10.8.0.10:8000/information')
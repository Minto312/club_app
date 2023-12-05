from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import Message_table

class Information(View):

    def get(self,request):
        messages_id = Message_table.objects.order_by('send_date').reverse().values('message_id')
        message_context_list = []
        
        for message_id in messages_id:
            message = Message_table.objects.get(message_id=message_id['message_id'])
            message_context = [f'''<div id="message-id-{str(message_id)}" class="message-wrap">''']

            if message.text_message :
                message_context.append(f'<div class="text-message"><p>{message.text_message}</p></div>')
            if message.image_message :
                message_context.append(f'<div class="image-message"><img src="/media/{message.image_message}"></div>')
            if message.file_message :
                message_context.append(f'<div class="file-message"><a href="/media/{message.file_message}" download="{message.file_message.name}">{message.file_message.name}</a></div>')
            message_context_list.append(''.join(message_context))
        context = {'messages':message_context_list}

        return render(request,'information/information.html', context)

    def post(self,request):

        text_message = request.POST['text-message']
        image_message = request.FILES['image-message']
        file_message = request.FILES['file-message']

        Message_table.objects.create(text_message=text_message, image_message=image_message, file_message=file_message)

        messages_id = Message_table.objects.order_by('send_date').reverse().values('message_id')
        message_context_list = []
        for message_id in messages_id:
            message = Message_table.objects.get(message_id=message_id['message_id'])
            message_context = [f'''<div id="message-id-{str(message_id)}" class="message-wrap">''']

            if message.text_message :
                message_context.append(f'<div class="text-message"><p>{message.text_message}</p></div>')
            if message.image_message :
                message_context.append(f'<div class="image-message"><img src="/media/{message.image_message}"></div>')
            if message.file_message :
                message_context.append(f'<div class="file-message"><a href="/media/{message.file_message}" download="{message.file_message.name}">{message.file_message.name}</a></div>')
            message_context_list.append(''.join(message_context))
        context = {'messages':message_context_list}

        return render(request,'information/information.html', context)
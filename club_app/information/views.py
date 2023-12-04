from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import Message_table

class Information(View):

    def get(self,request):
        message = Message_table.objects.order_by('send_date').reverse().values('file_message')
        print(message)
        f'''
            <div id="message-id-{message}" class="message-wrap">
                <div class="text-message">
                    {message}
                </div>
                <div class="image_message">
                    <img src="{message}">
                </div>
                <div class="file_message">
                    <a href="{message}" download="">file name</a>
                </div>
            </div>
        '''
        

        return render(request,'information/information.html')

    def post(self,request):
        return render(request,'information/information.html')
    

    #create_message
    def create_message(self, text_message, image_message, file_message):
        Message_table.objects.create(text_message=text_message, image_message=image_message, file_message=file_message)
    
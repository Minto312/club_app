from django.shortcuts import render
from django.views import View

# Create your views here.
class Information(View):
    def get(self,request):
        return render(request,'information/information.html')
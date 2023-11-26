from django.shortcuts import render, HttpResponse, redirect
from django.views import View

class Information(View):

    def get(self,request):
        return render(request,'information/information.html')

    def post(self,request):
        return render(request,'information/information.html')
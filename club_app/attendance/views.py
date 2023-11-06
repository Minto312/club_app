from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import AttendanceDB
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class Attendance(LoginRequiredMixin,View):

    def get(self,request):
        # すべてのレコードを表示
        select_all = AttendanceDB.objects.all()

        return_data =  {
            'posted':'you until do not post',
            'records':select_all
        }
        
        return render(request,'attendance/attendance.html',return_data)

    def post(self,request):
        print('==============\n\nposted run\n\n============')

        date = request.POST['date']
        print(f'============\n\n{date}\n\n===========')

        # ボタンから日付を登録
        insert_data =  {
            'name':request.user.username,
            'date':date,
            'attended':True
        }
        insertion = AttendanceDB(**insert_data)
        insertion.save()

        return_data = {'posted':'you posted!'}

        return render(request,'attendance/attendance.html',return_data)



import json
from datetime import datetime
def data(request):
    print(f'==============\n\nrun data\n\n============')

    current_year = datetime.now().year
    current_month = datetime.now().month
    username = request.user.username

    extract_condition = {
        'name':username,
        'date__year':current_year,
        'date__month':current_month
    }
    # 今月の出席した日付を抽出
    attended_dates = AttendanceDB.objects.filter(**extract_condition).order_by('date')

    attended_days = list()
    for record in attended_dates:
        date = record.date
        day = date.day
        attended_days.append(day)

    return_data = json.dumps(attended_days)
    print(f'==================\n\n/data/  {return_data=}\n\n=================')
    return HttpResponse(return_data)


@login_required
def qr(request):
    print(f'=============\n\nacceced QR\n\n{request.user.username=} \n\n===============')

    username = request.user.username

    # アクセスした際のユーザーと日付で登録
    insert_data =  {
        'name':username,
        'date':datetime.now(),
        'attended':True
    }
    AttendanceDB.objects.create(**insert_data)

    # .../attendance へリダイレクト
    return redirect('../')
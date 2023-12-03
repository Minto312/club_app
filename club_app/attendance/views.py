from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import AttendanceDB, ScheduleDB
# Create your views here.

class Attendance(View):
    def get(self,request):
        return render(request,'attendance/attendance.html')

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
import pytz
def attendance_data(request, year, month):
    print(f'==============\n\nrun data\n\n============')

    username = request.user.username

    extract_condition = {
        'name': username,
        'date__year': year,
        'date__month': month
    }
    # 今月の出席した日付を抽出
    attended_dates = AttendanceDB.objects.filter(**extract_condition).order_by('date')

    attended_days = dict()
    for record in attended_dates:
        date = record.date.astimezone(pytz.timezone('Asia/Tokyo'))
        attend_condition = 'attend' if record.attended else 'absent'
        attended_days[date.day] = attend_condition

    return_data = json.dumps(attended_days)
    print(f'==================\n\n/data/  {return_data=}\n\n=================')
    return HttpResponse(return_data)


def attend(request, is_attend):
    print(f'=============\n\naccessed QR\n\n{request.user.username=} \n\n===============')

    username = request.user.username

    # アクセスした際のユーザーと日付で登録
    print(f'=============\n\n{is_attend=}\n\n===============')
    print(f'=============\n\n{bool(is_attend)=}\n\n===============')
    insert_data =  {
        'name':username,
        'date':datetime.now(),
        'attended': is_attend == 'True'
    }
    
    if not AttendanceDB.objects.filter(
        name=username,
        date__year=datetime.now().year,
        date__month=datetime.now().month,
        date__day=datetime.now().day
    ).exists():
        AttendanceDB.objects.create(**insert_data)

    # .../attendance へリダイレクト
    return redirect('attendance:attendance')


class Activity(View):

    def get(self, request):
        # すべてのレコードを表示
        select_all = ScheduleDB.objects.all()  # 予定表のレコードを取得

        return_data =  {
            'posted':'you until do not post',
            'records':select_all
        }
        
        return render(request, 'attendance/activity.html', return_data)

    def post(self, request):
        # 新しいレコードを作成
        date = request.POST.get('date')
        # ボタンから日付を登録
        insert_data =  {
            'date':date,
            'has_club_activity':True
        }
        insertion = ScheduleDB(**insert_data)
        insertion.save()
        return redirect('information')

def activity_data(request, year, month):
    extract_condition = {
        'year': year,
        'month': month
    }
    # 今月の予定を抽出
    scheduled_dates = ScheduleDB.objects.filter(**extract_condition)

    if scheduled_dates.exists():
        scheduled_days = scheduled_dates[0].days
    else:
        scheduled_days = 'None'
    return_data = scheduled_days
    print(f'==================\n\n/data/  {return_data=}\n\n=================')
    return HttpResponse(return_data)

import re
def register(request, year: int, month: int):
    print(f'=============\n\naccessed register\n\n{request.user.username=} \n\n===============')

    days = request.POST['days']
    print(f'=============\n\n{days=}\n\n===============')
    insert_data =  {
        'year': year,
        'month': month,
        'days': days,
    }
    if not ScheduleDB.objects.filter(
        year=year,
        month=month
    ).exists():
        ScheduleDB.objects.create(**insert_data)
    else:
        ScheduleDB.objects.filter(
            year=year,
            month=month
        ).update(**insert_data)

    return HttpResponse('success')
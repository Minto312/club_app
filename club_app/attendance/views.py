from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import AttendanceDB, ScheduleDB
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# Create your views here.

class Attendance(View):

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

    attended_days = list()
    for record in attended_dates:
        date = record.date.astimezone(pytz.timezone('Asia/Tokyo'))
        day = date.day
        attended_days.append(day)

    return_data = json.dumps(attended_days)
    print(f'==================\n\n/data/  {return_data=}\n\n=================')
    return HttpResponse(return_data)


def attend(request):
    print(f'=============\n\naccessed QR\n\n{request.user.username=} \n\n===============')

    username = request.user.username

    # アクセスした際のユーザーと日付で登録
    insert_data =  {
        'name':username,
        'date':datetime.now(),
        'attended':True
    }
    if not AttendanceDB.objects.filter(
        name=username,
        date__year=datetime.now().year,
        date__month=datetime.now().month,
        date__day=datetime.now().day
    ).exists():
        AttendanceDB.objects.create(**insert_data)

    # .../attendance へリダイレクト
    return redirect('../')


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
        has_club_activity = request.POST.get('has_club_activity') == 'true'
        # ボタンから日付を登録
        insert_data =  {
            'date':date,
            'has_club_activity':True
        }
        insertion = ScheduleDB(**insert_data)
        insertion.save()
        return redirect('information')

def activity_data(request, year, month):
    print(f'==============\n\nrun data\n\n============')

    extract_condition = {
        'year': year,
        'month': month
    }
    # 今月の予定を抽出
    scheduled_dates = ScheduleDB.objects.filter(**extract_condition)

    if scheduled_dates.exists():
        scheduled_days = list(scheduled_dates[0].days)
    else:
        scheduled_days = 'None'
    # scheduled_days = list()
    # for record in scheduled_date\s:
    #     date = record.date.astimezone(pytz.timezone('Asia/Tokyo'))
    #     day = date.day
    #     scheduled_days.append(day)
        
    return_data = json.dumps(scheduled_days)
    print(f'==================\n\n/data/  {return_data=}\n\n=================')
    return HttpResponse(return_data)

def register(request, year: int, month: int, days: str):
    print(f'=============\n\naccessed QR\n\n{request.user.username=} \n\n===============')

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

    return redirect('../')
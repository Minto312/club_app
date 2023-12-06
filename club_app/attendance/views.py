import logging
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import AttendanceDB, ScheduleDB
# Create your views here.

logger = logging.getLogger(__name__)
class Attendance(View):
    def get(self,request):
        logger.info(f'User {request.user.username} accessed attendance')
        return render(request,'attendance/attendance.html')


import json
from datetime import datetime
import pytz
def attendance_data(request, year, month):
    logger.info(f'User {request.user.username} accessed attendance data')
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
    logger.debug(f'User {request.user.username} accessed attendance data: {return_data}')
    return HttpResponse(return_data)


def attend(request, is_attend):
    logger.info(f'User {request.user.username} accessed attend')
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
        logger.info(f'User {request.user.username} accessed activity')
        # すべてのレコードを表示
        select_all = ScheduleDB.objects.all()  # 予定表のレコードを取得

        return_data =  {
            'posted':'you until do not post',
            'records':select_all
        }
        
        return render(request, 'attendance/activity.html', return_data)


def activity_data(request, year, month):
    logger.info(f'User {request.user.username} accessed activity data')
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
        
    logger.debug(f'User {request.user.username} accessed activity data: {scheduled_days}')
    return HttpResponse(scheduled_days)


def register(request, year: int, month: int):
    logger.info(f'User {request.user.username} accessed register')

    days = request.POST['days']
    insert_data =  {
        'year': year,
        'month': month,
        'days': days,
    }
    
    try:
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
    except Exception as e:
        logger.exception(f'User {request.user.username} failed to register activity data: {insert_data}\n{e}')

    logger.debug(f'User {request.user.username} registered activity data: {insert_data}')
    return HttpResponse('success')
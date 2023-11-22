from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import ScheduleDB  # 予定表のモデルを使用
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import json
from datetime import datetime

class Information(LoginRequiredMixin, View):

    def get(self, request):
        # すべてのレコードを表示
        select_all = ScheduleDB.objects.all()  # 予定表のレコードを取得

        return_data =  {
            'posted':'you until do not post',
            'records':select_all
        }
        
        return render(request, 'information/calendar.html', return_data)

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

def information_data(request):
    print(f'==============\n\nrun data\n\n============')

    current_year = datetime.now().year
    current_month = datetime.now().month

    extract_condition = {
        'date__year':current_year,
        'date__month':current_month
    }
    # 今月の予定を抽出
    scheduled_dates = ScheduleDB.objects.filter(**extract_condition).order_by('date')

    scheduled_days = list()
    for record in scheduled_dates:
        date = record.date
        day = date.day
        has_club_activity = record.has_club_activity  # 部活動の有無を取得
        scheduled_days.append((day, has_club_activity))  # 日付と部活動の有無をタプルとして保存

    return_data = json.dumps(scheduled_days)
    print(f'==================\n\n/data/  {return_data=}\n\n=================')
    return HttpResponse(return_data)
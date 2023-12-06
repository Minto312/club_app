import logging
from venv import create, logger
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from account.models import CustomUser
#from club_app import score
from .models import ExamDB,ScoreDB
# Create your views here.

logger = logging.getLogger(__name__)
class Score(View):
    def get(self,request):
        logger.info(f'User {request.user.username} accessed score')
        
        score = ScoreDB.objects.filter(user=request.user)

        context = {
            'score':score
        }
        print(score)

        return render(request,'score/score.html',context)
    
class Recording(View):
    def get(self,request):
        exams = ExamDB.objects.all()

        context = {
            'exams':exams
        }

        return render(request,'score/recording.html',context)
    
    def post(self,request):
        logger.info(f'User {request.user.username} posted score')
        if ExamDB.objects.filter(exam_name=request.POST['exam-name']).exists():
            exam = ExamDB.objects.get(exam_name=request.POST['exam-name'])  
            score = ScoreDB.objects.create(
                user=request.user,
                exam_name=exam,
                score=request.POST['score']
            )
            score.save()
        else :
            exam = ExamDB.objects.create(exam_name=request.POST['exam-name'])
            exam.save
            score = ScoreDB.objects.create(
                user=request.user,
                exam_name=exam,
                score=request.POST['score']
            )
            score.save()
            logger.debug(f'User {request.user.username} posted score {request.POST["exam-name"]} {request.POST["score"]}')
        return redirect('score:score')
    

class exam_label(View):
    def get(self,request):
        exam_label_val = list(ExamDB.objects.all().values_list('exam_name', flat=True))
        logger.debug(f'User {request.user.username} accessed exam_label {exam_label_val}')
        return JsonResponse(exam_label_val, safe=False)

class exam_data(View):
    def get(self, request, exam_name):
        exam = ExamDB.objects.get(exam_name=exam_name)
        exam_data_val = [(CustomUser.objects.get(id=userid).username, score) for userid, score in exam.exam_id.all().values_list('user_id', 'score')]
        logger.debug(f'User {request.user.username} accessed exam_data {exam_data_val}')
        return JsonResponse(exam_data_val, safe=False)

class exam_chart(View):
    def get(self,request, exam_name):
        exam = ExamDB.objects.get(exam_name=exam_name)
        exam_chart_user = [CustomUser.objects.get(id=userid).username for userid in exam.exam_id.all().values_list('user_id', flat=True)]
        exam_chart_score = list(exam.exam_id.all().values_list('score', flat=True))
        logger.debug(f'User {request.user.username} accessed exam_chart {exam_chart_user} {exam_chart_score}')
        return JsonResponse([exam_chart_user, exam_chart_score], safe=False)

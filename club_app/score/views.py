from venv import create
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

#from club_app import score
from .models import ExamDB,ScoreDB
# Create your views here.

class Score(View):
    def get(self,request):
        score = ScoreDB.objects.filter(user=request.user)

        context = {
            'score':score
        }
        print(score)

        return render(request,'score/view.html',context)
    
class Recording(View):
    def get(self,request):
        exams = ExamDB.objects.all()

        context = {
            'exams':exams
        }

        return render(request,'score/recording.html',context)
    
    def post(self,request):
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
        return redirect('score:score')
    

class exam_label(View):
    def get(self,request):
        exam_label_val = list(ExamDB.objects.all().values_list('exam_name', flat=True))
        return JsonResponse(exam_label_val, safe=False)

class exam_data(View):
    def get(self, request, exam_name):
        exam = ExamDB.objects.get(exam_name=exam_name)
        exam_data_val = list(exam.exam_id.all().values_list('user', 'score'))
        return JsonResponse(exam_data_val, safe=False)

class exam_chart(View):
    def get(self,request, exam_name):
        exam = ExamDB.objects.get(exam_name=exam_name)
        exam_chart_user = list(exam.exam_id.all().values_list('user', flat=True))
        exam_chart_score = list(exam.exam_id.all().values_list('score', flat=True))
        return JsonResponse([exam_chart_user, exam_chart_score], safe=False)
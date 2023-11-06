from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ExamDB,ScoreDB
# Create your views here.

class Score(LoginRequiredMixin, View):
    def get(self,request):
        score = ScoreDB.objects.filter(user=request.user)

        context = {
            'score':score
        }
        print(score)

        return render(request,'score/score.html',context)
    
class Recording(LoginRequiredMixin, View):
    def get(self,request):
        exams = ExamDB.objects.all()

        context = {
            'exams':exams
        }

        return render(request,'score/recording.html',context)
    
    def post(self,request):
        exam = ExamDB.objects.get(exam_name=request.POST['exam-name'])
        score = ScoreDB.objects.create(
            user=request.user,
            exam_name=exam,
            score=request.POST['score']
        )
        score.save()
        return redirect('score:score')
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import CustomUser, Profile
# Create your views here.

class Register(View):
    def get(self,request):
        return render(request,'account/register.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user_data = {
            'username':username,
            'password':password,
        }

        user = CustomUser.objects.create_user(**user_data)

        login(request,user=user)

        return redirect('/account/mypage')

class SignIn(View):
    def get(self,request):
        return render(request,'account/sign_in.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        # 認証成功
        if user is not None:
            login(request,user)
            return_data = {'auth_message':'success!'}

            if 'next' in request.GET:
                # 元居たリンクへ遷移
                prev_link = request.GET['next']
                return redirect(prev_link)
            else:
                # マイページへ遷移
                return redirect('/account/mypage')

        else:
            return_data = {'auth_message':'アカウントが存在しないか、パスワードが間違っています'}
            return render(request,'account/sign_in.html',return_data)

class SignOut(View):
    def get(self,request):
        print(f'=========\n\nsign_outed\n\n=================')
        logout(request)
        return redirect('/account/sign_in')

class MyPage(LoginRequiredMixin,View):
    def get(self,request):
        try:
            profile = Profile.objects.get(user=request.user)
        except:
            profile = Profile.objects.create(user=request.user,name='',class_id='')

        return_data = {
            'username':request.user.username,
            'name' : profile.name,
            'class_id' : profile.class_id,
        }
        return render(request,'account/MyPage.html',return_data)

    def post(self,request):
        print(f'=========\n\nmypage_posted\n\n=================')

        username = request.POST['username']
        name = request.POST['name']
        class_id = request.POST['class_id']

        user = request.user
        # profileを選択
        profile = Profile.objects.get(user=user)

        user.username = username
        user.save()
        profile.name = name
        profile.class_id = class_id
        profile.save()

        return_data = {
            'username' : user.username,
            'name' : profile.name,
            'class_id' : profile.class_id,
        }
        print(f'=========\n\n{return_data}\n\n=================')
        return render(request,'account/MyPage.html',return_data)
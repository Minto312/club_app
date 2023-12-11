import logging
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import CustomUser, Profile
# Create your views here.

logger = logging.getLogger(__name__)
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
        
        logger.info(f'User {user.username} registered')
        return redirect('/account/mypage')

import os
class SignIn(View):
    def get(self,request):
        if not CustomUser.objects.all().exists():
            admin_password = os.environ.get('admin_password')
            CustomUser.objects.create_superuser('admin', admin_password)
        return render(request,'account/sign_in.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        # 認証成功
        if user is not None:
            login(request,user)
            logger.info(f'User {user.username} signed in')

            if 'next' in request.GET:
                # 元居たリンクへ遷移
                prev_link = request.GET['next']
                return redirect(prev_link)
            else:
                # マイページへ遷移
                return redirect('/home')

        else:
            logger.warning(f'User {username} failed to sign in with password {password}')
            return_data = {'auth_message':'アカウントが存在しないか、パスワードが間違っています'}
            return render(
                request,'account/sign_in.html',return_data)
    

class SignOut(View):
    def get(self,request):
        logout(request)
        logger.info(f'User {request.user.username} signed out')
        return redirect('/account/sign_in')

class MyPage(View):
    def get(self,request):
        try:
            profile = Profile.objects.get(user=request.user)
        except:
            profile = Profile.objects.create(user=request.user,name='',class_id='')

        return_data = {
            'username':request.user.username,
            'name' : profile.name,
            'class_id' : profile.class_id,
            'profile_image' : profile.profile_image,
        }
        return render(request,'account/MyPage.html',return_data)

    def post(self,request):
        logger.info(f'User {request.user.username} updated profile')

        username = request.POST['username']
        name = request.POST['name']
        class_id = request.POST['class_id']
        profile_image = request.FILES['profile_image']

        # profileを選択
        profile = Profile.objects.get(user=request.user)

        request.user.username = username
        request.user.save()
        profile.name = name
        profile.class_id = class_id
        profile.profile_image = profile_image
        profile.save()

        return_data = {
            'username' : username,
            'name' : profile.name,
            'class_id' : profile.class_id,
            'profile_image' : profile.profile_image,
        }
        logger.debug(return_data)
        return render(request,'account/MyPage.html',return_data)
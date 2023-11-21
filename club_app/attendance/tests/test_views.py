from django.shortcuts import redirect
from django.test import TestCase
from attendance.models import AttendanceDB
from datetime import datetime
from django.contrib.auth import get_user_model

class Tests(TestCase):
    def setUp(self):
        # テスト用アカウントの作成
        self.password = 'password123'
        self.test_user = get_user_model().objects.create_user(
            username='test_user0',
            password=self.password
        )
        # テスト用アカウントをログインさせる
        self.client.login(username=self.test_user.username, password=self.password)
        self.now = datetime.now()
        AttendanceDB.objects.create(
            name='test_user',
            date=self.now,
            attended=True
        )
        AttendanceDB.objects.create(
            name='test_user2',
            date=self.now,
            attended=True
        )
    def tearDown(self):
        # テスト用アカウントの作成
        self.password = 'password123'
        self.test_user = get_user_model().objects.create_user(
            username='test_user0',
            password=self.password
        )
        # テスト用アカウントをログインさせる
        self.client.login(username=self.test_user.username, password=self.password)
        self.now = datetime.now()
        AttendanceDB.objects.create(
            name='test_user',
            date=self.now,
            attended=True
        )
        AttendanceDB.objects.create(
            name='test_user2',
            date=self.now,
            attended=True
        )
        
    def test_attendance(self):
        redirect('attendance:qr')
        attends = AttendanceDB.objects.filter(name='test_user')
        print(attends)
        self.assertEqual(len(attends), 2)
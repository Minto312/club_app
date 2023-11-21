from django.test import TestCase
from attendance.models import AttendanceDB
from datetime import datetime

class PostModelTests(TestCase):
    def setUp(self):
        self.now = datetime.now()
        AttendanceDB.objects.create(
            name='test_user',
            date=self.now,
            attended=True
        )
    def tearDown(self):
        AttendanceDB.objects.create(
            name='test_user',
            date=self.now,
            attended=True
        )

    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをテスト"""
        post = AttendanceDB()
        name = 'test_user'
        attended = True
        
        post.name = name
        post.date = self.now
        post.attended = attended
        post.save()

        saved_posts = AttendanceDB.objects.all()
        actual_attend = saved_posts[0]

        self.assertEqual(actual_attend.name, name)
        self.assertEqual(actual_attend.date, self.now.astimezone())
        self.assertEqual(actual_attend.attended, attended)
import profile
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.apps import apps
from django.utils import timezone
import uuid
# from django.utils.translation import gettext_lazy as _ #多言語対応

# Create your models here.

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,username,password,is_staff,is_superuser):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser
            )
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_user(self,username,password):
        return self._create_user(username,password,False,False)
    
    def create_superuser(self,username,password):
        return self._create_user(username,password,True,True)
    
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    username = models.CharField(
        ('username'),
        max_length=50,
        unique=True,
        help_text='この項目は必須です。全角文字、半角英数字、@/./+/-/_ で50文字以下にしてください。',
        validators=[username_validator],
        error_messages={
            'unique': ("既に存在するユーザー名です"),
        },
    )

    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        abstract = False

    # def clean(self):
    #     super().clean()
    #     self.email = self.__class__.objects.normalize_email(self.email)

def image_name(instance, filename):
    print(f'====================\n\n{instance.user.username}\n\n====================')
    return f'profile_icon/{instance.user.username}.jpg'

class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    name = models.CharField(max_length=50, blank=True)
    class_id = models.CharField(max_length=4, blank=True)
    profile_image = models.ImageField(upload_to=image_name,blank=True)
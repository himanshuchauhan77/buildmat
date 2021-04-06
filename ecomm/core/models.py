from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.


class PhoneModel(models.Model):
    mobile = models.IntegerField(blank=False, unique=True)
    is_verified = models.BooleanField(default=False)


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, phone_no, password,
                     is_staff, is_superuser, **kwargs):
        if not email:
            raise ValueError('Users must have an email address or email')
        if not phone_no:
            raise ValueError('Users must have an email address or phone_no')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            phone_no=phone_no,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, phone_no, password, **kwargs):
        return self._create_user(email, phone_no,
                                 password, False, False, **kwargs)

    def create_superuser(self, email, phone_no, password, **kwargs):
        user = self._create_user(email, phone_no,
                                 password, True, True, **kwargs)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255,
                                unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics/',
                                    null=True, blank=True)
    phone_no = models.OneToOneField(PhoneModel,
                                    on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(blank=True, null=True)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone_no']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    objects = CustomUserManager()

    def __str__(self):
        return self.email

from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser, PermissionsMixin
# Create your models here.
from django.utils import timezone

class UserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError("The given email must be set")

        now = timezone.now()
        email = UserManager.normalize_email(email)
        user = self.model(email=email,
                        is_staff=false,
                        is_active=True,
                        is_superuser=False,
                        last_login=now,
                        created_at=now,
                        **extra_fields
                        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,password, **extra_fields):

        superuser = self.create_user(email,password, **extra_fields)
        superuser.is_staff = True
        superuser.is_active = True
        superuser.is_superuser = True    
        superuser.is_email_verified = True
        return superuser

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=80, blank=True, null=True)
    grade = models.CharField(max_length=125,blank=True,null=True)
    sector = models.CharField(max_length=125, blank=True,null=True)
    user_type = models.CharField(max_length=125,blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    profile_image_url = models.CharField(max_length=125,blank=True,null=True)
    department = models.CharField(max_length=125,blank=True,null=True)
    line_manager= models.CharField(max_length=255, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=False,editable=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=False,editable=True)        

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.full_name

    objects = UserManager()

    @classmethod
    def as_tuple(cls):
        return((item.value,item.name.replace('_',' ')) for item in cls)


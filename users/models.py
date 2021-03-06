# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username


# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
#     PermissionsMixin


# class UserManager(BaseUserManager):

#     def create_user(self, username, password=None, **extra_fields):
#         '''Creates and saves a new user'''
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     '''Custom user model that points'''
#     points = models.IntegerField(default=0)
#     username = models.CharField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'

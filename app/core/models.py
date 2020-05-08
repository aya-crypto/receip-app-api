from django.db import models

from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.conf import settings
# Create your models here.
class UserManager(BaseUserManager):
    """docstring for UserManager."""
    def create_user (self , email ,password =None, **extra_fields):
        """ creates and saves a new user """
        if not email:
            raise ValueError("Uers must have an email address")
        user =self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password):
        """create and saves a new superuser"""
        user = self.create_user(email,password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser,PermissionsMixin):
    """custom user model that supports using emails instead username."""
    email = models.EmailField(max_length=255 ,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD ='email'

class Tag(models.Model):
    """docstring for Tag."""

    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

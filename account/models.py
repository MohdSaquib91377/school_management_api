from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser,PermissionsMixin,TimeStampModel):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    name = models.CharField(_("name"), max_length=64)
    city = models.CharField(_("city"), max_length=64)
    pin_code = models.PositiveBigIntegerField(_("pin code"), max_length=32)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","city","pin_code"]

    objects = UserManager()

    class Meta:
        ordering = ("-created_at",)
        
    def __str__(self):
        return self.email
    

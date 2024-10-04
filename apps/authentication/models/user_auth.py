from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from apps.base.models.base import BaseModel


class CustomUser(AbstractBaseUser, BaseModel):
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    class Meta:
        db_table = "custom_user"

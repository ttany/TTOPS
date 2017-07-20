#_*_coding:utf-8_*_
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    phone = models.CharField(max_length=11,null=False)

    #users_images=models.ImageField(null=True)

from django.db import models
from django.shortcuts import redirect, reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

from django.contrib.auth.models import User

from rest_framework.reverse import reverse as api_reverse


# Create your models here.
class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")

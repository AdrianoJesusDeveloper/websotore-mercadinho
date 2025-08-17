from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class TimeStampModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True) 
    update_at = models.DateTimeField(auto_now=True)

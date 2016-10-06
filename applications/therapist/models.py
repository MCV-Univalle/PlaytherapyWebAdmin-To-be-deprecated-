from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Therapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    id_type = models.CharField(max_length=64)
    id_num = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    

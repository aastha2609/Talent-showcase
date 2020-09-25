from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=22)
    email=models.EmailField(max_length=22)
    phone=models.IntegerField()
    desc=models.TextField()
    def __str__(self):
       return self.name

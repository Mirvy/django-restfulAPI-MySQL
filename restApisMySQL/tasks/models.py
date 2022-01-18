from django.db import models
import datetime

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    scope = models.CharField(max_length=64)
    email = models.EmailField()
    notes = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Task(models.Model):
    description = models.CharField(max_length=150)
    body = models.CharField(max_length=500)
    urgent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    due = models.DateTimeField()
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)


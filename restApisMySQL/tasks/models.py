from django.db import models

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=150)
    body = models.CharField(max_length=500)
    urgent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    due = models.DateTimeField(auto_now_add=True)
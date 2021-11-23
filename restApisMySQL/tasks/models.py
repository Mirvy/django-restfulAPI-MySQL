from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=150)
    body = models.CharField(max_length=500)
    urgent = models.BooleanField(default=False)
from django.db import models

# Create your models here.

class student_info(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    contactno=models.CharField(max_length=15)
    
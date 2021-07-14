from django.db import models
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
# Create your models here.


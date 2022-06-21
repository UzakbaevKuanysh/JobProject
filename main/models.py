from tkinter import CASCADE
from django.db import models

from mysite import settings

# Create your models here.

class Boss(models.Model):
    name = models.CharField(max_length=100,blank = True)

    def __str__(self):
        return self.name
class Worker(models.Model):
    
    name = models.CharField(max_length=100,blank = True);
    major = models.CharField(max_length=100, blank= True);
    work_date = models.DateField(blank = True)
    salary = models.FloatField(max_length=50, blank = True, verbose_name="salary($)");
    boss = models.ForeignKey(Boss, blank = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


from django.db import models

# Create your models here.

class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    
class Employees(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    photo_file_name = models.CharField(max_length=100)
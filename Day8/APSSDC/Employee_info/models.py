from django.db import models

# Create your models here.
class Emp_data(models.Model):
	name=models.CharField(max_length=30,null=True)
	age=models.IntegerField(null=True)
	salary=models.FloatField(null=True)
	desig=models.CharField(max_length=30,null=True)
	address=models.CharField(max_length=100,null=True)
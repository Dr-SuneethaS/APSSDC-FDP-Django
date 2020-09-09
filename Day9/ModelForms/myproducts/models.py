from django.db import models

# Create your models here.
class Products(models.Model):
	types=[('Fashion','fashion'),('Electronics','electronics'),('Home','home')]
	p_name=models.CharField(max_length=100)
	p_cost=models.IntegerField()
	p_wight=models.IntegerField()
	p_type=models.CharField(max_length=30,choices=types)
	p_date=models.DateTimeField(auto_now_add = True,null=True)
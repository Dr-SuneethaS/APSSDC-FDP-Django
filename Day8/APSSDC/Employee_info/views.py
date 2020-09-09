from django.shortcuts import render,redirect
from Employee_info.models import Emp_data
from django.http import HttpResponse
# Create your views here.
def store(request):
	if request.method=="POST":
		f_name=request.POST['name']
		f_age=request.POST['age']
		f_salary=request.POST['salary']
		f_desig=request.POST['desig']
		f_address=request.POST['address']
		Emp_data.objects.create(name=f_name,age=int(f_age),salary=float(f_salary),desig=f_desig,address=f_address)
		return redirect('display')
	return render(request,'mytemplates/store.html')
def display(request):
	data=Emp_data.objects.all()
	return render(request,'mytemplates/display.html',{"mydata":data})
def update(request,id):
	data=Emp_data.objects.get(id=id)
	if request.method=="POST":
		f_name=request.POST['name']
		f_age=request.POST['age']
		f_salary=request.POST['salary']
		f_desig=request.POST['desig']
		f_address=request.POST['address']
		data.name=f_name
		data.age=f_age
		data.salary=f_salary
		data.address=f_address
		data.desig=f_desig
		data.save()
		return redirect('display')
	return render(request,'mytemplates/update.html',{'mydata':data})
def updateit(request,name):
	data=Emp_data.objects.get(name=name)
	if request.method=="POST":
		f_name=request.POST['name']
		f_age=request.POST['age']
		f_salary=request.POST['salary']
		f_desig=request.POST['desig']
		f_address=request.POST['address']
		data.name=f_name
		data.age=f_age
		data.salary=f_salary
		data.address=f_address
		data.desig=f_desig
		data.save()
		return redirect('display')
	return render(request,'mytemplates/update.html',{'mydata':data})
def  delete(request,id):
	data=Emp_data.objects.get(id=id)
	data.delete()
	return redirect('display')
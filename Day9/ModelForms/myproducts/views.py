from django.shortcuts import render,redirect
from myproducts.forms import Myclass
from myproducts.models import Products
from django.http import HttpResponse
# Create your views here.
def addproduct(request):
	if request.method=="POST":
		data=Myclass(request.POST)
		data.save()
		return redirect('showproducts')
	form=Myclass()
	return render(request,'mytemplates/addproducts.html',{'form':form})
def showproducts(request):
	data=Products.objects.all()
	return render(request,'mytemplates/showproducts.html',{'data':data})
def update(request,id):
	data=Products.objects.get(id=id)
	if request.method=="POST":
		data=Myclass(request.POST,instance=data)
		data.save()
		return redirect('showproducts')
	form=Myclass(instance=data)
	return render(request,'mytemplates/update.html',{'form':form,'data':data})
def delete(request,id):
	data=Products.objects.get(id=id)
	data.delete()
	return redirect('showproducts')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def register(request):
	if request.method=="POST":
		f_name=request.POST['f_name']
		l_name=request.POST['l_name']
		gmail=request.POST['gmail']
		phn=request.POST['ph_no']
		username=request.POST['username']
		password=request.POST['password']
		data={
			'first_name':f_name,
			'last_name':l_name,
			'Gmail':gmail,
			'phone_number':phn,
			'username':username,
			'password':password
		}
		# print(f_name,l_name,gmail,phn,username,password)
		return render(request,'mytemplates/mydata.html',data)
	return render(request,'mytemplates/register.html')

def login(request):
	return render(request,'mytemplates/login.html')

def home(request):
	return render(request,'mytemplates/home.html')

def aboutpage(request):
	return render(request,'mytemplates/about.html')
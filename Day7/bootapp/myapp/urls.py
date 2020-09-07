from django.urls import path
from myapp import views

urlpatterns = [
	path('register/',views.register,name='register'),
    path('login/',views.login,name="lg"),
    path('',views.home,name="hme"),
    path('about/',views.aboutpage,name="abt")
]
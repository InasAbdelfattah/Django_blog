from django.shortcuts import render

# Create your views here.
def home(request):
	context ={"hi":'hellow'}
	return render(request,'myapp/index.html',context)
def regist(request):
	context ={"hi":'welcome on registration'}
	return render(request,'myapp/regist.html',context)
def login(request):
	context ={"hi":'welcome on login form'}
	return render(request,'myapp/login.html',context)
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
	

	context={}
	context['var1']="this is the line printed directly through views"

	context={'var2':'var2 is here through views','var3':'var3 is here '}

	list_1=[]
	list_1.append('hello')
	list_1.append('how')
	list_1.append('are ')
	list_1.append('you.')

	context['list_1']=list_1
	return render(request,'ank/dashboard.html',context)

def store(request):
	context={}
	return render(request,'ank/store.html',context)

def cart(request):
	context={}
	return render(request,'ank/cart.html',context)

def checkout(request):
	context={}
	return render(request,'ank/checkout.html',context)

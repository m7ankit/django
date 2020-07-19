from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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
	products = Product.objects.all()
	context={'products':products}
	return render(request,'ank/store.html',context)

def cart(request):
	if request.user.is_authenticated:
		customer=request.user.customer #this os to set one to one rekationship
		order,created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
	else:
		items=[]
		items={'get_cart_total':0,'get_items_total':0}



	context={'items':items,'order':order}
	return render(request,'ank/cart.html',context)

def checkout(request):
	if request.user.is_authenticated:
		customer=request.user.customer 
		order,created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
	else:
		items=[]
		items={'get_cart_total':0,'get_items_total':0}



	context={'items':items,'order':order}

	return render(request,'ank/checkout.html',context)

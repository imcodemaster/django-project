from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404
from .models import * 
from django.urls import reverse_lazy 
# Create your views here.

def home (request):
	return render(request, 'info/index.html')

def about (request):
	return render(request, 'info/about.html')

def portfolio (request):
	return render(request, 'info/portfolio.html')


def pricing (request):
	return render(request, 'info/pricing.html')

def services (request):
	return render (request, 'info/services.html')
	
def shop(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'info/products.html',context)


def team (request):
	return render (request, 'info/team.html')
	

class ContactView(CreateView):
	model = Contact
	fields = ['first_name', 'second_name' ,  'email' , 'mobile' , 'message' ] #describe the field need to create 
	success_url = reverse_lazy('home')



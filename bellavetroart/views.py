from django.shortcuts import render
from .models import 
# Create your views here.

def contact(request):
	return render(request, "bellavetoart/contact.html")
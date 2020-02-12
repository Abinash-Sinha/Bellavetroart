from django.shortcuts import render
from .models import Contact
# Create your views here.

def contact(request):
	contact_us = Contact.objects.all()
	return render(request, 'bellavetroart/contact.html', {'contact_us' : contact_us})
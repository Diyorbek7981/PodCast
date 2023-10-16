from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import *
from .forms import *


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class ContactView(CreateView):
    template_name = 'contact.html'
    model = Contact
    form_class = ContactForm





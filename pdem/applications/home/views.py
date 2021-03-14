from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from applications.category.models import Category

class Home(ListView):
    model = Category
    template_name = 'home/home.html'
    # paginate_by = 3

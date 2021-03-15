from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from applications.category.models import Category
from applications.product.models import Product

class Home(ListView):
    context_object_name = 'category_list'
    queryset = Category.objects.filter(is_published=True)
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the top products
        context['product_list'] = Product.objects.filter(is_top=True)
        print("Aqui debe de haber un context")
        print(context)
        return context

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from applications.category.models import Category
from applications.product.models import Product, Variant

class Home(ListView):
    context_object_name = 'categories_list'
    queryset = Category.objects.filter(is_published=True)
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the top products
        context['products_list'] = Product.objects.filter(is_top=True)
        return context

class Products(ListView):
    context_object_name = 'products_list'
    model = Product
    paginate_by = 9
    template_name = 'home/products.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet of all the variants
        context['variants_list'] = Variant.objects.all()

        # Add in a QuerySet of all the categories
        context["categories_list"] = Category.objects.filter(is_published=True)

        if 'category' in self.request.GET:
            category = self.request.GET.get('category', '')
            if category:
                context["category_filter"] = Category.objects.filter(id=category)

        return context

    def get_queryset(self):
        context = Product.objects.order_by('name')

        # Keywords
        if 'kword' in self.request.GET:
            kword = self.request.GET.get('kword', '')
            if kword:    
                context = context.filter(name__icontains=kword)

        # Categories
        if 'category' in self.request.GET:
            category = self.request.GET.get('category', '')
            if category:
                context = context.filter(category__id=category)

        return context


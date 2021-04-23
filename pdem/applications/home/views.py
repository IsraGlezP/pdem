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
    paginate_by = 12
    template_name = 'home/products.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet of all the variants
        context['variants_list'] = Variant.objects.all()

        # Add in a QuerySet of all the categories
        context["categories_list"] = Category.objects.filter(is_published=True)

        paginator = context.get('paginator')
        num_pages = paginator.num_pages
        current_page = context.get('page_obj')
        page_no = current_page.number

        if num_pages <= 11 or page_no <= 6:
            pages = [x for x in range(1, min(num_pages + 1, 12))]
        elif page_no > num_pages - 6:
            pages = [x for x in range(num_pages - 10, num_pages + 1)]
        else:  # case 3
            pages = [x for x in range(page_no - 5, page_no + 6)]

        context.update({'pages': pages})

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


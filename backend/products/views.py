from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView
from .models import Product, Category


class ProductsListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class CategoryListView(View):
    def get(self, request, slug, *args, **kwargs):
        context = Product.objects.filter(categories__url=slug, is_published=True)
        return render(request, "products/product_list.html", {'products': context})

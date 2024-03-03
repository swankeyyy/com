from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView
from .models import Product, Category, Brand, Tag


class ProductsListView(ListView):
    """All products at the home page"""

    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class CategoryListView(View):
    """Products by categories"""
    def get(self, request, slug, *args, **kwargs):
        context = Product.objects.filter(categories__url=slug, is_published=True)
        return render(request, "products/product_list.html", {'products': context})


class PageTitleSearchResultsView(View):
    def get(self, request):
        query = request.GET.get("q")
        products = Product.objects.filter(name__icontains=query)
        return render(request, "products/product_list.html", {"products": products})



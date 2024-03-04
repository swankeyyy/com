from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView
from .models import Product, Category, Brand, Tag


class ProductsListView(View):
    """All products at the home page"""

    def get(self, request):
        content = Product.objects.filter(is_published=True)
        return render(request, "products/product_list.html", {'products': content})


class CategoryListView(View):
    """Products by categories"""

    def get(self, request, slug, *args, **kwargs):
        context = Product.objects.filter(categories__url=slug, is_published=True)
        return render(request, "products/product_list.html", {'products': context})


class PageTitleSearchResultsView(View):
    """Queryset of results searched from top searchfield on page"""

    def get(self, request):
        query = request.GET.get("q")
        products = Product.objects.filter(name__icontains=query)
        return render(request, "products/product_list.html", {"products": products})


class FilteredProductsView(View):
    """Filtered products by brand or tag or by tag and brand
        html all in templatetags, by the Q and | it works like python "or"
    """

    def get(self, request):
        content = Product.objects.filter(
            Q(brand__name__in=request.GET.getlist("brand")) |
            Q(tag__name__in=request.GET.getlist("tag"))
        )
        return render(request, "products/product_list.html", {"products": content})


class SortedView(View):
    """Sort products view, it get value from form and ordering by it"""
    def get(self, request, *args, **kwargs):
        value = request.GET.get("sorting")

        if value:
            content = Product.objects.all().order_by(value)
        else:
            content = Product.objects.all().order_by('id')
        return render(request, "products/product_list.html", {'products': content})

from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView
from .models import Product, Category, Brand, Tag


class ProductsListView(View):
    """All products at the home page"""

    def get(self, request, **kwargs):
        query = request.GET.get("q")
        tags = any(request.GET.getlist("brand") or request.GET.getlist("tag"))
        content = Product.objects.filter(is_published=True)
        if query:
            content = content.filter(name__icontains=query)
        elif tags:
            content = content.filter(
                Q(brand__name__in=request.GET.getlist("brand")) |
                Q(tag__name__in=request.GET.getlist("tag"))
            )

        return render(request, "products/product_list.html", {'products': content})


class CategoryListView(View):
    """Products by categories"""

    def get(self, request, **kwargs):
        slug = kwargs['slug']
        context = Product.objects.filter(categories__url=slug, is_published=True)
        return render(request, "products/product_list.html", {'products': context})




class SortedView(View):
    """Sort products view, it get value from form and ordering by it"""

    def get(self, request, *args, **kwargs):
        value = request.GET.get("sorting")

        if value:
            content = Product.objects.all().order_by(value)
        else:
            content = Product.objects.all().order_by('id')
        return render(request, "products/product_list.html", {'products': content})


class ProductDetailView(View):
    """Detail Product Page"""

    template_name = "products/product-detail.html"

    def get(self, request, *args, **kwargs):
        slug = kwargs['slug']
        content = Product.objects.get(url=slug)
        last_products = Product.objects.filter(is_published=True)[0:2]
        return render(request, self.template_name, {'product': content, "last_products": last_products})

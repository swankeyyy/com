from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Product, Category, Brand, Tag
from django.views.generic.base import ContextMixin
from comments.forms import CommentForm


class ProductsListView(View):
    """All products at the home page.
    it filters by tags and gives searched results"""

    def get_content_by_form(self, data):
        query = data.GET.get("q")
        tags = any(data.GET.getlist("brand") or data.GET.getlist("tag"))
        content = Product.objects.filter(is_published=True)
        if query:
            content = content.filter(name__icontains=query)
        elif tags:
            content = content.filter(
                Q(brand__name__in=data.GET.getlist("brand")) |
                Q(tag__name__in=data.GET.getlist("tag"))
            )
        return content

    def get(self, request, **kwargs):
        content = self.get_content_by_form(request)
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


class ProductDetailView(DetailView):
    """Detail Product Page"""
    model = Product
    template_name = "products/product-detail.html"
    form = CommentForm()
    slug_field = "url"
    context_object_name = "product"

    def get_last_products(self):
        return Product.objects.order_by("-id")[0:2]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_object().comments.order_by('-id')
        context['form'] = self.form
        context['test'] = 'abc'
        return context

from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from common.views import CommonTitleMixin
from .models import Product, Category
from comments.forms import CommentForm
from django.core.paginator import Paginator
from basket.models import Order


class ProductsListView(CommonTitleMixin, View):
    """All products at the home page.
    it filters by tags and gives searched results"""
    title = 'Главная'

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
        return render(request, "products/product_list.html", {'products': content, 'title': self.title})


class CategoryListView(View):
    """Products by categories"""
    title = None

    def get(self, request, **kwargs):
        slug = kwargs['slug']
        title = Category.objects.filter(url=slug)
        if title:
            self.title = title[0].name

        context = Product.objects.filter(categories__url=slug, is_published=True)

        return render(request, "products/product_list.html", {'products': context, 'title': self.title})


class SortedView(View):
    """Sort products view, it get value from form and ordering by it"""
    title = 'Результаты'

    def get(self, request, *args, **kwargs):
        value = request.GET.get("sorting")

        if value:
            content = Product.objects.all().order_by(value)
        else:
            content = Product.objects.all().order_by('id')
        return render(request, "products/product_list.html", {'products': content, 'title': self.title})


class ProductDetailView(DetailView):
    """Detail Product Page"""
    model = Product
    template_name = "products/product-detail.html"
    form = CommentForm()
    slug_field = "url"
    context_object_name = "product"

    def get_last_products(self):
        return Product.objects.order_by("-id")[0:8]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_object().comments.order_by('-id')
        context['form'] = self.form
        context['test'] = 'abc'
        context['title'] = self.get_object().name
        return context

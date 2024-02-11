from django.views.generic import ListView
from .models import Product


class ProductsListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

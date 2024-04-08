from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from products.models import Product
from .models import Order, OrderRow


def basket_remove(request, pk):
    """Delete item from user Order"""
    basket = OrderRow.objects.get(id=pk)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class BasketAdd(View):
    """Controller for add item into users cart."""
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        user = request.user
        order = Order.objects.get(user=user)
        if not order:
            order = Order.objects.create(user=user)
            OrderRow.objects.create(user=user, product=product, order=order)
        else:
            order_row = OrderRow.objects.filter(user=user, product=product, order=order)
            if not order_row:
                OrderRow.objects.create(user=user, product=product, order=order)
        print(*map(lambda x: int(x[0]), list(user.order.first().order_row.all().values_list("product_id"))))
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

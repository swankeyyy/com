from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from products.models import Product

from .models import Basket


class BasketAdd(View):
    """Controller for add item into users cart."""

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        user = request.user
        basket = Basket.objects.filter(product=product, user=user)
        if not basket.exists():
            Basket.objects.create(product=product, user=user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])



def basket_remove(request, pk):
    basket = Basket.objects.get(id=pk)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
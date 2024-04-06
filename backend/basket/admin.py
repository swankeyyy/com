from django.contrib import admin
from .models import Basket, Order, OrderRow


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "id")

@admin.register(OrderRow)
class OrderRowAdmin(admin.ModelAdmin):
    list_display = ("user", "product")
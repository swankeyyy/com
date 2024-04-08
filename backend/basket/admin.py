from django.contrib import admin
from .models import Order, OrderRow


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "id")

@admin.register(OrderRow)
class OrderRowAdmin(admin.ModelAdmin):
    list_display = ("user", "product")
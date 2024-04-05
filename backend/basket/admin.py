from django.contrib import admin
from .models import Basket


@admin.register(Basket)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")



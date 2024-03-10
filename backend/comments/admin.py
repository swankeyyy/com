from django.contrib import admin
from .models import Comment




@admin.register(Comment)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "create_at")

# Register your models here.

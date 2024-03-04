from django import template
from products.models import Category, Tag, Brand, Product
from django.db.models import Count

register = template.Library()


@register.inclusion_tag("products/tags/categories.html")
def get_all_categories():
    """all categories for top menu(on button canvas)"""
    content = Category.objects.all()
    return {"categories": content}

@register.inclusion_tag("products/tags/filter_by_tag.html")
def get_all_tags():
    content = Tag.objects.all().annotate(count=Count("games"))
    return {"tags": content}


@register.inclusion_tag("products/tags/filter_by_brand.html")
def get_all_brands():
    """Searched all brands and their count on related models"""
    content = Brand.objects.all().annotate(count=Count("games"))
    return {"brands": content}
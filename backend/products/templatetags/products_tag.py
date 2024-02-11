from django import template
from products.models import Category

register = template.Library()


@register.inclusion_tag("products/tags/categories.html")
def get_all_categories():
    content = Category.objects.all()
    return {"categories": content}

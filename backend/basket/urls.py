from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:pk>', views.BasketAdd.as_view(), name="basket_add_item"),
    path('remove/<int:pk>', views.basket_remove, name="basket_remove_item")
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name="main_page_view"),
    path('sorted/', views.SortedView.as_view(), name="sorted_view"),
    path('category/<slug:slug>', views.CategoryListView.as_view(), name="category_list"),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name="product_detail_view")
]
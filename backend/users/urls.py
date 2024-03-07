from django.urls import path
from . import views

urlpatterns = [
    path('sign/', views.SignView.as_view(), name="sign_view"),
    path('logout/', views.logout, name="logout")
]
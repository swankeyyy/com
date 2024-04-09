from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name="registration_view"),
    path('logout/', views.LogoutView.as_view(next_page=None), name="user_logout_view"),
    path('login/', views.UserLogInView.as_view(), name="user_login_view"),
    path('profile/<int:pk>', views.ProfileView.as_view(), name="user_profile_view")
]
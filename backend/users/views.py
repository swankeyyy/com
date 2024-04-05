from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.models import User
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.contrib.auth.views import LogoutView
from common.views import CommonTitleMixin

class UserLogInView(CommonTitleMixin, LoginView):
    """View for login authorization"""

    template_name = "users/login.html"
    form_class = UserLoginForm
    redirect_authenticated_user = True
    next = "main_page_url"
    title = 'Вход'






class RegistrationView(CommonTitleMixin, CreateView):
    """View for create new user(customer)"""

    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('user_login_view')
    title = 'Регистрация'




class ProfileView(CommonTitleMixin, UpdateView):
    """Profile View with chsnge only last_name and first_name and phone"""
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Профиль'

    def get_success_url(self):
        return reverse_lazy('main_page_view')



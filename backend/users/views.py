from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.models import User
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.views import LogoutView


class UserLogInView(LoginView):
    """View for login authorization"""

    template_name = "users/login.html"
    form_class = UserLoginForm
    redirect_authenticated_user = True
    next = "main_page_url"


class RegistrationView(CreateView):
    """View for create new user(customer)"""

    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('main_page_view')

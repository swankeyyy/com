from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from users.models import User
from .forms import UserRegistrationForm
from django.shortcuts import redirect
from django.contrib import auth


# class SignView(View):
#
#     def get(self, request):
#         registration_form = UserRegistrationForm()
#         return render(request, 'users/registration.html', {"registration_form": registration_form})
#
#
#     def post(self, request, **kwargs):
#         data = request.POST
#         registration_form = UserRegistrationForm(data)
#         if registration_form.is_valid():
#             print(registration_form.cleaned_data)
#             registration_form.save(phone=0)
#         else:
#             print(registration_form.cleaned_data)
#             registration_form = UserRegistrationForm()
#         return render(request, 'users/registration.html', {"registration_form": registration_form})


class SignView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('main_page_view')


def logout(request):
    auth.logout(request)
    return reverse_lazy('main_page_view')
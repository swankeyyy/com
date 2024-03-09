from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    """Form for login page"""

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control", 'id': "username",
        'placeholder': "Введите имя пользователя",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control", 'id': "password", 'placeholder': "Введите пароль",
        "type": "password",
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    """Form for users/registration page"""

    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': "usename", "name": "username", "class": "form-control",
        'placeholder': "Введите имя пользователя"
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': "first_name", "name": "first_name", "class": "form-control",
        'placeholder': "Введите имя"
    }), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': "last_name", "name": "last_name", "class": "form-control",
        'placeholder': "Введите фамилию"
    }), required=False)
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'id': "email", "name": "email",
        'placeholder': "Введите адрес почты", "class": "form-control",
        "type": "email"
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'id': "phone", "name": "phone",
        'placeholder': "Номер телефона", "type": "tel", "class": "form-control"
    }), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': "password", "name": "password", 'placeholder': "Введите пароль", "type": "password",
        "class": "form-control",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': "cpassword", "name": "cpassword", 'placeholder': "Подтвердите пароль", "type": "password",
        "class": "form-control",
    }))

    # image = forms.ImageField(widget=forms.FileInput(attrs={
    #     'class': "custom-file-input"
    # }), required=False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'phone', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': "first_name", "name": "first_name",
        'class': "form-control"

    }), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'id': "last_name", "name": "last_name",
        'class': "form-control"

    }), required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'id': "phone", "name": "phone",
         "class": "form-control"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': "username", "name": "username",
        'class': "form-control", 'readonly': True, "disable": "true"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'id': "email", "name": "email",
        'class': "form-control", 'readonly': True
    }))

    # image = forms.ImageField(widget=forms.FileInput(attrs={
    #     'class': "custom-file-input"
    # }), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name',  'username', 'email', 'phone')

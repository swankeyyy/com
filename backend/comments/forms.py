from django import forms
from .models import Comment
from products.models import Product
from users.models import User


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("text", )


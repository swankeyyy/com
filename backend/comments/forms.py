from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'id': "text", "name": "text", "class": "form-control comment",
        'placeholder': "Введите комментарий", "rows": "4", "cols": "50", "type": "text"
    }))


    class Meta:
        model = Comment
        fields = ("text",)


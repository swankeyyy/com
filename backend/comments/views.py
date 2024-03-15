from django.shortcuts import render, redirect
from django.views import View
from products.models import Product
from .forms import CommentForm
from .models import Comment


class AddComment(View):
    """Добавляет комментарий к странице товара
    в форме в урл прокидывается ид товара, пользователь берется из request,
    text  из формы.
    В планах реализовать создание комментария через form.save()"""

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=pk)
            user = request.user
            Comment.objects.create(product=product, user=user, text=request.POST.get('text'))
            return redirect("product_detail_view", product.url)


class DeleteComment(View):
    """Удаления комментарий по ид комментария.
    Разрешение стоит через проверку в шаблоне залогиненного пользователя по ид с владельцем комментария.
    Удаляется через Ид коммента в маршруте"""

    def get(self, request, **kwargs):
        comment = Comment.objects.get(id=kwargs['pk'])
        url = comment.product.url
        comment.delete()
        return redirect("product_detail_view", url)

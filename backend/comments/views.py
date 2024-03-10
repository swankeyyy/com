from django.shortcuts import render, redirect
from django.views import View
from products.models import Product
from .forms import CommentForm
from .models import Comment

class AddComment(View):

    def post(self, request, pk):

        form = CommentForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=pk)
            user = request.user
            Comment.objects.create(product=product, user=user, text=request.POST.get('text'))
            return redirect("product_detail_view", product.url)



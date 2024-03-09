from django.db import models
from products.models import Product
from users.models import User


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар", related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Комментатор", related_name="comments")
    parent = models.ForeignKey('self', verbose_name="Родитель", related_name="child", on_delete=models.CASCADE,
                               blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    text = models.TextField(max_length=400, verbose_name="Текст комментария")

    def __str__(self):
        return f'{self.product} - {self.user.name} - {self.text}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

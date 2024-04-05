from django.db import models
from users.models import User
from products.models import Product


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="basket", verbose_name="Пользователь")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Товар", related_name="basket",
                                null=True, blank=True)

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price

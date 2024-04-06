from django.db import models
from users.models import User
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="basket", verbose_name="Пользователь")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Товар", related_name="basket")

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт {self.product.name}'

    def sum(self):
        return self.product.price


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="order", verbose_name="Пользователь")

    def __str__(self):
        return f'чтото тут {self.user}'

class OrderRow(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="order_row", verbose_name="Пользователь")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Товар", related_name="order_row")
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Ячейка товара",
                              related_name="order_row")

    def __str__(self):
        return f'{self.user.username} for {self.product.name}'

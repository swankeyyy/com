from django.db import models
from users.models import User
from products.models import Product


# class Basket(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="basket", verbose_name="Пользователь")
#     product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Товар", related_name="basket")
#
#     def __str__(self):
#         return f'Корзина для {self.user.email} | Продукт {self.product.name}'
#
#     def sum(self):
#         return self.product.price


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="order", verbose_name="Пользователь")

    def __str__(self):
        return f'Корзина для {self.user.username}'

    def get_all_products(self):
        """Use for UI< when item is in order and need to deactivate 'Add button'"""

        products = Product.objects.filter(order_row__user_id=self.user.id)
        return products

    def get_total_sum(self):
        """Returns total sum of all products for User Order"""
        return sum(order_row.sum() for order_row in self.order_row.all())

class OrderRow(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="order_row", verbose_name="Пользователь")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Товар", related_name="order_row")
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Ячейка товара",
                              related_name="order_row")

    def __str__(self):
        return f'{self.user.username} for {self.product.name}'

    def sum(self):
        return self.product.price

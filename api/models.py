from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class ApiUser(AbstractUser):

    USER_TYPE_CHOICES = (
        ('supplier', 'Поставщик'),
        ('consumer', 'Потребитель'),
    )
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)
    #
    # groups = models.ManyToManyField(Group, related_name='api_users')
    # user_permissions = models.ManyToManyField(Permission, related_name='api_users')

    # def is_supplier(self):
    #     return self.user_type == 'supplier'
    #
    # def is_consumer(self):
    #     return self.user_type == 'consumer'
    #
    # def take_product(self, product_id):
    #     if self.is_consumer():
    #         try:
    #             product = Product.objects.get(id=product_id)
    #             if product.count > 0:
    #                 product.count -= 1
    #                 product.save()
    #                 return f"Товар {product.name} успешно взят со склада"
    #             else:
    #                 return "Товар закончился на складе"
    #         except Product.DoesNotExist:
    #             return "Товар не найден"
    #     else:
    #         return "Доступ запрещен"
    #
    # def supply_product(self, product_id):
    #     if self.is_supplier():
    #         try:
    #             product = Product.objects.get(id=product_id)
    #             product.count += 1
    #             product.save()
    #             return f"Товар {product.name} успешно добавлен на склад"
    #         except Product.DoesNotExist:
    #             return "Товар не найден"
    #     else:
    #         return "Доступ запрещен"


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    # product = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Product(models.Model):
    count = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, related_name="products", on_delete=models.CASCADE)


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class ApiUser(AbstractUser):

    USER_TYPE_CHOICES = (
        ('supplier', 'Поставщик'),
        ('consumer', 'Потребитель'),
    )
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    # product = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    count = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, related_name="products", on_delete=models.CASCADE)


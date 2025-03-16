from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название продавца")
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sellers"
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    MARKETPLACE_CHOICES = [
        ('OZON', 'OZON'),
        ('Wildberries', 'Wildberries'),
    ]

    # Основное поле с выбором маркетплейса
    marketplace = models.CharField(max_length=20, choices=MARKETPLACE_CHOICES)

    # Дополнительные данные товара храним в JSON-поле.
    details = models.JSONField(default=dict, blank=True)

    # Поле "продавец" теперь является внешним ключом к модели Seller
    seller = models.ForeignKey(
        Seller,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продавец",
        related_name="products"  # Позволяет получить список товаров продавца через seller.products.all()
    )

    created_at = models.DateTimeField(auto_now_add=True)

    # Поле для привязки менеджера (пользователя)
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,  # Если пользователь удалён, продукт сохраняется, но поле становится NULL
        null=True,
        blank=True,
        related_name="products"
    )

    def __str__(self):
        return f"{self.marketplace} - {self.pk}"
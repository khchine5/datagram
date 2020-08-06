from django.db import models
from .mixin import SeqNamedMixin

class Chain(SeqNamedMixin):
    address = models.CharField(verbose_name="Addresse", max_length=100)

    class Meta:
        app_label = 'product'
        verbose_name = "Chain"
        verbose_name_plural = "Chains"
        abstract = False

class Store(SeqNamedMixin):
    address = models.CharField(verbose_name="Addresse", max_length=100)
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)

    class Meta:
        app_label = 'product'
        verbose_name = "Store"
        verbose_name_plural = "Stores"
        abstract = False

class Product(SeqNamedMixin):
    barcode = models.CharField(
        verbose_name="Barcode", max_length=150, unique=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        app_label = 'product'
        verbose_name = "Product"
        verbose_name_plural = "Products"
        abstract = False

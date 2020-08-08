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
    description = models.TextField(verbose_name="Description", blank=True)
    price = models.FloatField(verbose_name="Price", default=0)
    stores = models.ManyToManyField(Store, verbose_name="Stores")

    class Meta:
        app_label = 'product'
        verbose_name = "Product"
        verbose_name_plural = "Products"
        abstract = False

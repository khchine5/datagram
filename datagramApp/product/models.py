from django.db import models
from .mixin import SeqNamedMixin

import cloudscraper
import json


headers = {'X-Requested-With': 'XMLHttpRequest'}

AVAILABILITY_CHOICES = [
    ('purchasable', 'Purchasable'),
    ('stopped', 'Stopped'),
    ('indispensable', 'Indispensable'),
]


class Chain(SeqNamedMixin):
    address = models.CharField(verbose_name="Addresse", max_length=100)
    website = models.URLField(verbose_name="Website", max_length=200, default='' )
    scrap_api = models.URLField(verbose_name="Scrap API", max_length=200, default='')

    def do_scrap_products(self):
        count = 0
        if self.scrap_api:
            scraper = cloudscraper.create_scraper()
            res = scraper.get(self.scrap_api.format(0), headers=headers).text
            res = json.loads(res)
            totalPage = res.get('meta').get('totalPage')
            for page in range(1,int(totalPage) + 1):
                res = scraper.get(self.scrap_api.format(page), headers=headers).text
                res = json.loads(res)
                for p in res.get('data', {}):
                    attributes = p.get('attributes', {})
                    price = attributes.get('price', {})
                    prod, created = Product.objects.get_or_create(
                        barcode=attributes.get('ean'))
                    
                    prod.name = attributes.get('title', '')
                        # availability= ,
                    prod.packaging =  attributes.get('packaging', '')
                    prod.url = "{}{}".format(self.website, p.get('links').get('self'))
                    prod.price = price.get('perUnit',0)
                    prod.unitOfMeasure = price.get('unitOfMeasure', '')
                    #prod.objects.update(**prodData)
                    prod.save()
                    count += 1

        return count

    class Meta:
        app_label = 'product'
        verbose_name = "Chain"
        verbose_name_plural = "Chains"
        abstract = False


class Store(SeqNamedMixin):
    address = models.CharField(verbose_name="Addresse", max_length=100)
    chain = models.ForeignKey(
        Chain, on_delete=models.CASCADE)

    class Meta:
        app_label = 'product'
        verbose_name = "Store"
        verbose_name_plural = "Stores"
        abstract = False


class ProductStores(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    startDate = models.DateField(verbose_name="Start date")


class Categories(SeqNamedMixin):

    code = models.CharField(verbose_name="Code", max_length=20)
    uri = models.CharField(verbose_name="URI", max_length=100)

    class Meta:
        app_label = 'product'
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        abstract = False


class Product(SeqNamedMixin):
    barcode = models.CharField(
        verbose_name="Barcode", max_length=150, unique=True)
    description = models.TextField(verbose_name="Description", blank=True)
    price = models.FloatField(verbose_name="Price", default=0)
    promotion = models.BooleanField(verbose_name="Promotion", default=False)
    packaging = models.CharField(verbose_name="Packaging", max_length=30, default='')
    url = models.URLField(verbose_name="URL", max_length=200, default='')
    stores = models.ManyToManyField(
        Store, through=ProductStores)
    availability = models.CharField(
        verbose_name="Availability", choices=AVAILABILITY_CHOICES, default='purchasable', max_length=15)
    unitOfMeasure = models.CharField(
        verbose_name="unitOfMeasure", max_length=20, default='')

    class Meta:
        app_label = 'product'
        verbose_name = "Product"
        verbose_name_plural = "Products"
        abstract = False

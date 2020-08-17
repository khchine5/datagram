from .models import Chain, Product, Store

import django_filters

class NameFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    active = django_filters.BooleanFilter()
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    stores = django_filters.ModelChoiceFilter(queryset=Store.objects.order_by('name'))



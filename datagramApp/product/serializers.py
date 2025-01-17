from .models import Chain, Product, Store
from rest_framework import serializers


class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

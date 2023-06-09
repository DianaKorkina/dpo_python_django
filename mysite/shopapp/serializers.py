from .models import Product, Order
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "pk",
            "name",
            "description",
            "price",
            "discount",
            "created_ad",
            "archived",
            "preview",
        )

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "pk",
            "delivery_address",
            "promocode",
            "created_ad",
            "user",
            "products",
            "receipt",
        )
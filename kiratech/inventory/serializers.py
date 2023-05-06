from rest_framework import serializers

from .models import *


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name')

    class Meta:
        model = Inventory
        fields = "__all__"

from rest_framework import serializers
from apps.inventory_mgmt.models.inventory import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["name", "description"]


class InventoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"

from django.urls import path
from apps.inventory_mgmt.views.inventory import InventoryMgmt

urlpatterns = [
    path("inventory/", InventoryMgmt.as_view(), name="inventory"),
    path("inventory/<uuid:pk>/", InventoryMgmt.as_view(), name="inventory_by_id"),
]

from django.db import models
from apps.base.models.base import BaseModel
from apps.authentication.models.user_auth import CustomUser


class Inventory(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class meta:
        db_table = "inventory_master"

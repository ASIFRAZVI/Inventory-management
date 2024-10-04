from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from apps.authentication.jwt_processor.jwt_decoder import decode_jwt_token
from apps.authentication.models.user_auth import CustomUser
from apps.inventory_mgmt.models.inventory import Inventory
from apps.inventory_mgmt.serializers.inventory_serializer import (
    InventorySerializer,
    InventoryReadSerializer,
)
from apps.base.serializers.base import UUIDFeildSerializer


class InventoryMgmt(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [decode_jwt_token]

    def post(self, request, *args, **kwargs):
        req_data = request.data
        user_id = request.user.id

        serializer = InventorySerializer(data=req_data)
        if not serializer.is_valid():
            return Response(
                {"error": "please provide the unique name & description"}, status=400
            )

        name = serializer.validated_data["name"]
        description = serializer.validated_data["description"]
        if Inventory.objects.filter(name=name).exists():
            return Response(
                {
                    "error": "the inventory obj already exists in db please provide the unique name & description"
                },
                status=400,
            )

        user_id_serializer = UUIDFeildSerializer(data={"id": user_id})
        if not user_id_serializer.is_valid():
            return Response({"error": "please provide valid token or uuid"}, status=400)

        # customer_obj = CustomUser.objects.get(id=user_id)
        # if customer_obj is None:
        #     return Response({"error": "user does not exists"}, status=400)
        try:
            customer_obj = CustomUser.objects.get(id=user_id)
        except:
            return Response({"error": "user does not exists"}, status=400)

        inventory_final_data = {
            "name": name,
            "description": description,
            "user": customer_obj,
        }

        inventory_data_obj = Inventory.objects.create(**inventory_final_data)
        inventory_data_obj.save()

        return Response({"message": "Inventory Created"}, status=201)

    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            inventory_obj = Inventory.objects.all()
            if inventory_obj is None:
                return Response({"message": "data does't exists"}, status=200)
            serializer = InventoryReadSerializer(inventory_obj, many=True)
            return Response(serializer.data, status=200)

        id_serializer = UUIDFeildSerializer(data={"id": pk})
        if not id_serializer.is_valid():
            return Response({"error": "please provide valid uuid"}, status=400)

        # inventory_object = Inventory.objects.get(id=pk)

        # if inventory_object is None:
        #     return Response({"message": "Inventory does't exists"}, status=200)

        try:
            inventory_object = Inventory.objects.get(id=pk)
        except:
            return Response({"message": "Inventory does't exists"}, status=200)

        serializers = InventoryReadSerializer(inventory_object)
        return Response(serializers.data, status=200)

    def put(self, request, pk=None, *args, **kwargs):
        if pk is None:
            return Response({"error": "please provide id"}, status=400)

        id_serializer = UUIDFeildSerializer(data={"id": pk})
        if not id_serializer.is_valid():
            return Response({"error": "please provide valid uuid"}, status=400)

        try:
            inventory_object = Inventory.objects.get(id=pk)
        except:
            return Response({"message": "Inventory does't exists"}, status=200)

        serializer = InventorySerializer(inventory_object, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response("Inventory Updated", status=200)

    def delete(self, request, pk=None, *args, **kwargs):
        if pk is None:
            return Response({"error": "please provide id"}, status=400)

        id_serializer = UUIDFeildSerializer(data={"id": pk})
        if not id_serializer.is_valid():
            return Response({"error": "please provide valid uuid"}, status=400)

        try:
            inventory_object = Inventory.objects.get(id=pk)
        except:
            return Response({"message": "Inventory does't exists"}, status=200)
        inventory_object.delete()
        return Response("Inventory deleted Succesfully! ", status=204)

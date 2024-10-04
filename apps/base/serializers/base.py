from rest_framework import serializers


# UUID Serializers
class UUIDFeildSerializer(serializers.Serializer):
    id = serializers.UUIDField()

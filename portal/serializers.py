from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    product = serializers.ListField(
        child=serializers.CharField(max_length=200))

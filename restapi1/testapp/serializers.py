from rest_framework import serializers

class ProductSerializers(serializers.Serializer):
    no = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.FloatField()
    qty = serializers.IntegerField()

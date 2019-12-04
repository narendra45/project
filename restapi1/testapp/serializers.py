from rest_framework import serializers
from testapp.models import ProductModel
from django.db.utils import IntegrityError


class ProductSerializers(serializers.Serializer):
    no = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.FloatField()
    qty = serializers.IntegerField()

    def create(self,valid_data):
        try:
            return ProductModel.objects.create(**valid_data)
        except IntegrityError as ie:
            raise ie
    def update(self,instance,valid_data):
        instance.no = valid_data.get("no",instance.no)
        instance.name = valid_data.get("name",instance.name)
        instance.price = valid_data.get("price",instance.price)
        instance.qty = valid_data.get("qty",instance.qty)

        instance.save()
        return instance

from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from testapp.models import ProductModel
from testapp.serializers import ProductSerializers
from rest_framework.renderers import JSONRenderer


class ReadOneProduct(View):
    def get(self,request):
        stream = io.BytesIO(request.body)
        d1 = JSONParser().parse(stream)
        one_product = ProductModel.objects.get(no=d1["pno"])
        ps = ProductSerializers(one_product)
        json_data = JSONRenderer().render(ps.data)
        return HttpResponse(json_data,content_type = 'application/json')

class ReadAllProducts(View):
    def get(self,request):
        qs = ProductModel.objects.all()
        ps = ProductSerializers(qs,many=True)
        json_data = JSONRenderer().render(ps.data)
        return HttpResponse(json_data,content_type ='application/json')

class ReadAllOneProducts(View):
    def get(self,request):
        stream = io.BytesIO(request.body)
        d1 = JSONParser().parse(stream)
        print(d1)
        if d1:
            one_product = ProductModel.objects.get(no=d1["pno"])
            ps = ProductSerializers(one_product)
            json_data = JSONRenderer().render(ps.data)
            return HttpResponse(json_data,content_type = 'application/json')
        else:
            qs = ProductModel.objects.all()
            ps = ProductSerializers(qs,many = True)
            json_data = JSONRenderer().render(ps.data)
            return HttpResponse(json_data,content_type = 'application/json')

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt,name="dispatch")
class InsertProduct(View):
    def post(self,request):
        stream = io.BytesIO(request.body)
        d1 = JSONParser().parse(stream)
        #sending data to serializers class to save it into the database
        ps = ProductSerializers(data=d1)
        if ps.is_valid():
            try:
                ps.save()
                message = {"msg":"Product is Saved"}
            except IntegrityError:
                message = {"msg":"Product No is Inavlid"}
        else:
            message = {"msg":"Product is not saved"}
        json_data = JSONRenderer().render(message)
        return HttpResponse(json_data,content_type="application/json")

@method_decorator(csrf_exempt,name="dispatch")
class UpdateProduct(View):
    def put(self,request):
        d1=JSONParser().parse(io.BytesIO(request.body))
        pro = ProductModel.objects.get(no=d1["no"])
        ps = ProductSerializers(pro,data=d1,partial=True)
        if ps.is_valid():
            ps.save()
            message = {"msg":"product updated Successfully"}
        else:
            message = {"msg":ps.errors}
        json_data = JSONRenderer().render(message)
        return HttpResponse(json_data,content_type="application/json")

@method_decorator(csrf_exempt,name="dispatch")
class DeleteProduct(View):
    def delete(self,request):
        ProductModel.objects.get(no=JSONParser().parse(io.BytesIO(request.body))["no"]).delete()
        message = {"msg":"Product Deleted Successfully"}
        return HttpResponse(JSONRenderer().render(message),content_type="application/json")

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from product.forms import ProductForms

# Create your views here.
from product.models import ProductDetails, Tags


def addProduct(request):
    form = ProductForms()
    if request.method=="POST":
        form = ProductForms(request.POST,request.FILES)

        if form.is_valid():
            productObj=form.save(commit=False)
            productObj.save()
            tags = request.POST.getlist('tags')
            tagsObj = [Tags.objects.get(id=tags) for tags in tags]
            for tagsObj1 in tagsObj:
                productObj.tags.add(tagsObj1)
                productObj.save()
            return HttpResponse("<h3>Product added Successfully!!!</h3> <a href='/accounts/home/'> Go Home</a>")
        print(form.errors)
        messages.info(request, 'product not added')
        return redirect('add_product')

    return render(request,'product/addproduct.html',{'form':form})



def viewAllProducts(request):
    productObj = ProductDetails.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(productObj, 2)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request,'product/viewall.html',{'products':products})


def editProduct(request,product_id):
    product = get_object_or_404(ProductDetails, pk=product_id)
    if request.method == "POST":
        form = ProductForms(request.POST,instance=product)
        if form.is_valid():
            studObj = form.save(commit=False)
            studObj.save()
            return HttpResponse("<h3>Product Updated Successfully!!!</h3> <a href='/accounts/home/'> Go Home</a>")
    else:
        form = ProductForms(instance=product)
    return render(request, 'product/edit.html', {'form': form})


def deleteProduct(request,product_id):
    ProductDetails.objects.get(id=product_id).delete()

    return HttpResponse("<h3>Product Updated Successfully!!!</h3> <a href='/accounts/home/'> Go Home</a>")
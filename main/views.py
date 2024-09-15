from django.shortcuts import render, redirect  
from django.http import HttpResponse
from django.core import serializers 
from main.forms import ProductForm
from main.models import Product


def show_main(request):
    products = Product.objects.all()
    
    context = {
        'npm' : '2306212096',
        'name': 'Trias Fahri Naufal',
        'class': 'PBP B',

        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
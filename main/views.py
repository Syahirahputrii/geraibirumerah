from django.shortcuts import render, redirect
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers

# Create your views here.
# def show_main(request):
#     context = {
#         'name' : 'Jacket',
#         'price': 'Rp 100.000,00',
#         'description': 'Lengan panjang dan memiliki hoodie'
#     }

#     return render(request, "main.html", context)


def show_main(request):
    products = Product.objects.all()
    context = {
        'name': 'Syahirah Putri Aisyah',
        'price': 'Rp 100.000,00',
        'description': 'Lengan panjang dan memiliki hoodie',
        'products': products,
        'total_products': products.__len__(),
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)    

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")    

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")    

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")    
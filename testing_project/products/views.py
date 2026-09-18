from django.db.models import Model
from django.shortcuts import render
from products.models import Product
# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def product(request):
    products = Product.objects.all()
    context  = {
        'products' : products
    }

    return render(request, template_name="products.html", context=context)
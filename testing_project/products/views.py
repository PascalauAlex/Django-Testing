from django.contrib.auth.decorators import login_required
import requests
from django.http import JsonResponse, HttpResponse
from requests.exceptions import RequestException
from products.forms import ProductForm
from django.shortcuts import render, redirect
from products.models import Product

# Create your views here.



def post(request):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        response.raise_for_status()
    except RequestException as e:
        # Log the error in a real application


        # Return a 503 Service Unavailable response
        return HttpResponse('Service unavailable', status=503)

    return JsonResponse(response.json())

@login_required
def profile(request):
    return render(request, "profile.html")

def login(request):
    return render(request,"login.html")


def homepage(request):
    return render(request, 'index.html')


def product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
        else:
            context = {
                'products': Product.objects.all(),
                'form': form
            }
            return render(request, template_name="products.html", context=context)

    products = Product.objects.all()
    context  = {
        'products' : products,
        'form':ProductForm(),
    }
    return render(request, template_name="products.html", context=context)


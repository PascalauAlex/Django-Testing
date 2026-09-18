
from django.contrib import admin
from django.urls import path
from products import views
from products.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('products',views.product, name="products")
]

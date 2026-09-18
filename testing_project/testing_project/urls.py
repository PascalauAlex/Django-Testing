
from django.contrib import admin
from django.urls import path
from products import views
from products.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('products/',views.product, name="products"),
    path('profile',views.profile, name="profile"),
    path('login/',views.login, name='login'),
    path('post', views.post, name='post'),
]

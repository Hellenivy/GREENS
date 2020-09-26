from django.urls import path
from .views import product_list
from .views import product_upload
from .views import product_details
from .import views

urlpatterns = [
    path('', product_list, name='product-list'),
    path('products/<int:product_id>/',product_details,name="product_details"),
    path('products/upload/', product_upload, name='product-upload'),
]
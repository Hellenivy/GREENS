from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm


def product_list(request):
    product = Product.objects.all()
    return render(request, 'product_list.html', {'product': product})



# def upload_product(request):
#     form=ProductForm()
#     if request.method == "POST":
#          form = ProductForm(request.POST,request.FILES)
#          if form.is_valid():
#             form.save()
#          return redirect('product_list')
#     else:
#        form = ProductForm
#        return render(request, 'upload_product.html', {'form': form})


def product_details(request,product_id):
    product=Product.objects.get(id=product_id)
    return render(request,'product_details.html',{'product':product})


def product_upload(request):
    form = ProductForm()
    if request.method == "POST":
         form = ProductForm(request.POST,request.FILES)
         if form.is_valid():
            form.save()
         return redirect('product-list')
    else:
       form = ProductForm()
       return render(request, 'upload_product.html', {'form': form})






















































































    
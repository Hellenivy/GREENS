
from django.shortcuts import render,redirect
from .forms import KioskForm

# Create your views here.

def kiosk_upload(request):
    if request.method == "POST":
         form = KioskForm(request.POST,request.FILES)
         if form.is_valid():
            form.save()
         return redirect('product_list')
    else:
       form = KioskForm
       return render(request, 'kiosk_upload.html', {'form': form})


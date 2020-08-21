

# Register your models here.
from django.contrib import admin
from .models import Kiosk, KioskOwner

admin.site.register(KioskOwner)
admin.site.register(Kiosk)

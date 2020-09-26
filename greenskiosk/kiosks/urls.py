from django.urls import path
from .views import kiosk_upload
from .import views

urlpatterns = [
    path('kiosks/upload/', kiosk_upload, name='kiosk_upload'),
]
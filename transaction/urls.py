from django.urls import path
from .views import verify_payment

urlpatterns = [
    path('callback/', verify_payment, name='payment_verify'),
]

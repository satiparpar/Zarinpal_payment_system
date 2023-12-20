from django.urls import path
from .views import verify_payment, home, initiate_payment

urlpatterns = [
    path('', home, name='home'),
    path('payment/', initiate_payment, name='initiate_payment'),
    path('callback/', verify_payment, name='payment_verify'),
]

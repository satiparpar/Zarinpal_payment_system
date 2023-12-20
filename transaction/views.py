from django.conf import settings
from django.http import HttpResponse
import requests
from django.shortcuts import redirect, render
from .models import Transaction


def initiate_payment(request):
    amount = 1000000
    callback_url = settings.ZARINPAL_CALLBACK_URL

    payload = {
        'merchant_id': settings.ZARINPAL_MERCHANT_ID,
        'amount': amount,
        'callback_url': callback_url,
        'description': 'It is a test of payment system',
    }

    response = requests.post('https://www.zarinpal.com/pg/rest/WebGate/PaymentRequest.json', json=payload)
    if response.json()['Status'] == 100 or 101:
        authority = response.json()['Authority']
        Transaction.objects.create(amount=amount, payment_status='Pending', authority=authority)
        return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}')


def verify_payment(request):
    if request.GET.get('Status') == 'OK':
        authority = request.GET.get('Authority')
        transaction = Transaction.objects.get(authority=authority)
        verification_data = {
            'merchant_id': settings.ZARINPAL_MERCHANT_ID,
            'authority': authority,
            'amount': transaction.amount,
        }

        verification_response = requests.post('https://www.zarinpal.com/pg/rest/WebGate/PaymentVerification.json',
                                              json=verification_data)

        if verification_response.json()['Status'] == 100 or 101:
            transaction.payment_status = 'Success'
            transaction.save()
            return HttpResponse('Payment was successful.')
        else:
            transaction.payment_status = 'Failed'
            transaction.save()
            return HttpResponse('Payment verification failed.')
    else:
        return HttpResponse('Payment failed or cancelled by user.')


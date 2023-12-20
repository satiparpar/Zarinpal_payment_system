from django.contrib.auth.models import User
from django.db import models


class Transaction(models.Model):
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20)

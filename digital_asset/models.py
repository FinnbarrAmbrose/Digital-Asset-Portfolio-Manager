from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class CryptoAsset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=8)
    purchase_date = models.DateField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
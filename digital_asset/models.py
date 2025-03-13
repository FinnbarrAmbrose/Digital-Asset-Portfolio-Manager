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

    def total_value(self):
        return self.quantity * self.current_price if self.current_price else None

    def profit_loss(self):
        return (self.current_price - self.purchase_price) * self.quantity if self.current_price else None

    def __str__(self):
        return f"{self.name} - {self.user.username}"
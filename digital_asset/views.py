from django.shortcuts import render, redirect
from .models import CryptoAsset
from .forms import AssetForm


def portfolio(request):
    assets = CryptoAsset.objects.filter(user=request.user)
    return render(request, 'digital_asset/portfolio.html', {'assets': assets})
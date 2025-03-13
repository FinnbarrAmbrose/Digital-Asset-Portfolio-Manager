from django.test import TestCase
from django.contrib.auth.models import User
from .models import CryptoAsset

class CryptoAssetTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        CryptoAsset.objects.create(user=user, name="Bitcoin", purchase_price=50000, quantity=0.1)

    def test_asset_creation(self):
        asset = CryptoAsset.objects.get(name="Bitcoin")
        self.assertEqual(asset.purchase_price, 50000)
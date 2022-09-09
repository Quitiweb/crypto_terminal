from rest_framework import serializers
from crypto_tools.models import CryptoCoin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCoin
        fields = "__all__"

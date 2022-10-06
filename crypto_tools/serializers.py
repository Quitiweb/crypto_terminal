from rest_framework import serializers
from crypto_tools.models import CryptoCoin


class ClosePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCoin
        fields = ('name', 'symbol', 'date', 'close')


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCoin
        fields = "__all__"


class CoinListSerializer(serializers.Serializer):
    name = serializers.CharField()
    symbol = serializers.CharField()
    cc_count = serializers.IntegerField()


class PricesAndDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCoin
        fields = ('date', 'close')

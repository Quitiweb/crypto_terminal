from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

import crypto_tools.serializers as ser
from crypto_tools.models import CryptoCoin


class CoinsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = CryptoCoin.objects.all()
    serializer_class = ser.CoinSerializer
    permission_classes = [IsAuthenticated]

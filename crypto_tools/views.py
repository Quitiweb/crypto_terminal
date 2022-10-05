from django.db.models import Count
from django.http import JsonResponse
from django.views import View
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import crypto_tools.serializers as ser
from crypto_tools.models import CryptoCoin


class CoinsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
        Returns all the Crypto Coins registered in the DataBase
    """
    queryset = CryptoCoin.objects.all()
    serializer_class = ser.CoinSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['GET'], url_path=r'by_symbol/(?P<symbol>\w+)', detail=False)
    def coins_by_symbol(self, request, symbol):
        """
            Returns a list of Crypto Coins filtered by the given Symbol
        """
        cc_filtered = CryptoCoin.objects.filter(symbol=symbol)
        serializer = self.get_serializer(cc_filtered, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CoinsListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
        Returns the list of Crypto Coins by name
    """
    queryset = CryptoCoin.objects.values('name', 'symbol').annotate(
        cc_count=Count('name'))
    serializer_class = ser.CoinListSerializer
    permission_classes = [IsAuthenticated]


class ClosePriceViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
        Endpoint to return the Close price value for the given coin symbol and date
    """
    serializer_class = ser.ClosePriceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        symbol = self.kwargs['symbol']
        cdate = self.kwargs['date']

        return CryptoCoin.objects.filter(symbol=symbol, date__contains=cdate)


class MinMaxDatesViewSet(View):
    """
        Returns the minimum and maximum dates
    """
    def get(self, request):
        min_date = CryptoCoin.objects.earliest('date').date
        max_date = CryptoCoin.objects.latest('date').date

        return JsonResponse({'min_date': min_date,
                             'max_date': max_date})

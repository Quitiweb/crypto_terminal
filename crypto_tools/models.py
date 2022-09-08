from django.db import models


class CryptoCoin(models.Model):
    serial_number = models.IntegerField(default=1)
    name = models.CharField(max_length=150, default="")
    symbol = models.CharField(max_length=100, default="")
    date = models.DateTimeField(db_index=True)
    high = models.FloatField(default=0)
    low = models.FloatField(default=0)
    open = models.FloatField(default=0)
    close = models.FloatField(default=0)
    volume = models.FloatField(default=0)
    market_cap = models.FloatField(default=0)

    class Meta:
        verbose_name = 'CryptoCoin'
        verbose_name_plural = 'CryptoCoins'
        unique_together = ('serial_number', 'name', )

    def __str__(self):
        return "{} {}".format(self.serial_number, self.name)

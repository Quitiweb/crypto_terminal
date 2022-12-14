from django.contrib import admin

from crypto_tools import models


@admin.register(models.CryptoCoin)
class CryptoCoinAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'name', 'symbol', 'high', 'low', 'open', 'close', )
    readonly_fields = ("serial_number", )
    list_filter = ('name', )

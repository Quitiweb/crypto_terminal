from django.contrib import admin

from crypto_tools import models

# Register your models here.
admin.site.register([models.CryptoCoin])

from django.urls import include, path
from rest_framework.routers import DefaultRouter

import crypto_tools.views as api_views

router = DefaultRouter()
router.register('coins', api_views.CoinsViewSet, basename='coins')
router.register('coins/list_symbols', api_views.CoinsViewSet, basename='list_symbols')

urlpatterns = [
    path('', include(router.urls)),
]

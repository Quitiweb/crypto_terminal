from django.urls import include, path
from rest_framework.routers import DefaultRouter

import crypto_tools.views as api_views

router = DefaultRouter()
router.register('coins', api_views.CoinsViewSet, basename='coins')

urlpatterns = [
    path('', include(router.urls)),
]

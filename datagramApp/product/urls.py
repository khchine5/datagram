from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, ChainViewSet, StoreViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'chain', ChainViewSet)
router.register(r'store', StoreViewSet)


urlpatterns = router.urls
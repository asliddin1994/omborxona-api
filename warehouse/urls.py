from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, MaterialViewSet, ProductMaterialViewSet, WarehouseViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'product-materials', ProductMaterialViewSet)
router.register(r'warehouses', WarehouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

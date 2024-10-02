from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, MaterialViewSet, ProductMaterialViewSet, WarehouseViewSet, ProductMaterialsAPIView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'product-materials', ProductMaterialViewSet)
router.register(r'warehouses', WarehouseViewSet)

urlpatterns = [
    path('product-materials/<int:product_id>/<int:qty>/', ProductMaterialsAPIView.as_view(), name='product-materials'),
    path('', include(router.urls)),
]

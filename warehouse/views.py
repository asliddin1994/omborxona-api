from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Product, Material, ProductMaterial, Warehouse
from .serializers import ProductSerializer, MaterialSerializer, ProductMaterialSerializer, WarehouseSerializer

class ProductMaterialsAPIView(APIView):
    def get(self, request, product_id, qty):
        # Mahsulotni olish, agar topilmasa 404 qaytarish
        product = get_object_or_404(Product, id=product_id)
        product_materials = ProductMaterial.objects.filter(product=product)

        result = {
            "product_name": product.name,
            "product_qty": qty,
            "product_materials": []
        }

        # Har bir mahsulot uchun kerak bo'lgan xomashyo va omborxonadagi miqdorni olish
        for product_material in product_materials:
            required_qty = product_material.quantity * qty
            material = product_material.material
            warehouses = Warehouse.objects.filter(material=material)

            for warehouse in warehouses:
                if required_qty <= 0:
                    break

                available_qty = warehouse.remainder
                if available_qty >= required_qty:
                    result['product_materials'].append({
                        "warehouse_id": warehouse.id,
                        "material_name": material.name,
                        "qty": required_qty,
                        "price": warehouse.price
                    })
                    required_qty = 0
                else:
                    result['product_materials'].append({
                        "warehouse_id": warehouse.id,
                        "material_name": material.name,
                        "qty": available_qty,
                        "price": warehouse.price
                    })
                    required_qty -= available_qty

            # Yetarlicha xomashyo yo'qligini qaytarish
            if required_qty > 0:
                result['product_materials'].append({
                    "warehouse_id": None,
                    "material_name": material.name,
                    "qty": required_qty,
                    "price": None
                })

        return Response(result)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class ProductMaterialViewSet(viewsets.ModelViewSet):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

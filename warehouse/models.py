from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.FloatField()  # Foydalaniladigan miqdor

    def __str__(self):
        return f"{self.product.name} - {self.material.name}"


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.FloatField()  # Omborda qolgan miqdor
    price = models.FloatField()  # Narx

    def __str__(self):
        return f"{self.material.name} - {self.remainder} left at {self.price}"



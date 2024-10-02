from django.db import models  # Django'dan models modulini import qilamiz, bu ma'lumotlar bazasi modellarini yaratishga yordam beradi.

# Mahsulot (Product) modeli
class Product(models.Model):
    name = models.CharField(max_length=100)  # Mahsulot nomi, maksimal 100 belgi
    code = models.CharField(max_length=100, unique=True)  # Mahsulot kodi, har bir mahsulot uchun unikaldir

    def __str__(self):
        return self.name  # Mahsulot nomini qaytaradi, bu foydalanuvchiga qulayroq ko'rsatish uchun

# Xomashyo (Material) modeli
class Material(models.Model):
    name = models.CharField(max_length=100)  # Xomashyo nomi, maksimal 100 belgi

    def __str__(self):
        return self.name  # Xomashyo nomini qaytaradi

# Mahsulot-Xomashyo (ProductMaterial) modeli
class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Mahsulotga bog'lanadi, agar mahsulot o'chirilsa, bu bog'lanish ham o'chiriladi
    material = models.ForeignKey(Material, on_delete=models.CASCADE)  # Xomashyoga bog'lanadi, agar xomashyo o'chirilsa, bu bog'lanish ham o'chiriladi
    quantity = models.FloatField()  # Foydalaniladigan xomashyo miqdori

    def __str__(self):
        return f"{self.product.name} - {self.material.name}"  # Mahsulot va xomashyo nomlarini birlashtirib ko'rsatadi

# Omborxona (Warehouse) modeli
class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)  # Xomashyoga bog'lanadi, agar xomashyo o'chirilsa, bu bog'lanish ham o'chiriladi
    remainder = models.FloatField()  # Omborda qolgan xomashyo miqdori
    price = models.FloatField()  # Xomashyoning narxi

    def __str__(self):
        return f"{self.material.name} - {self.remainder} left at {self.price}"  # Xomashyo nomi, qolgan miqdor va narxini birlashtirib ko'rsatadi

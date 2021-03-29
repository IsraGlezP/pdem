from django.db import models

# Import models
from applications.category.models import Category

class Product(models.Model):
    name = models.CharField('nombre', max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField('descripción', max_length=250, blank=True)
    photo_main = models.ImageField('imagen', upload_to='products/', blank=True)
    is_top = models.BooleanField('producto_top', default=False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']

    def __str__(self):
        return self.name

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField('valor', max_length=50)

    class Meta:
        verbose_name = 'Variante'
        verbose_name_plural = 'Variantes'
        ordering = ['product']

    def __str__(self):
        return self.product.name

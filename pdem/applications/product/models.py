from django.db import models

class Product(models.Model):
    product = models.CharField('producto', max_length=150)
    description = models.CharField('descripción', max_length=250, blank=True)
    photo_main = models.ImageField('imagen', upload_to='photos/products/', blank=True)
    is_top = models.BooleanField('producto top', default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['product']

    def __str__(self):
        return self.product

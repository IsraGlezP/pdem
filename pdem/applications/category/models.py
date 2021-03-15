from django.db import models

class Category(models.Model):
    name = models.CharField('nombre', max_length=150)
    description = models.CharField('descripción', max_length=250, blank=True)
    photo_main = models.ImageField('imagen', upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField('publicar', default=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name

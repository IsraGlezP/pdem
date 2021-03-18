# Generated by Django 3.1.7 on 2021-03-18 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0005_auto_20210318_0247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nombre')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='descripción')),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/products/', verbose_name='imagen')),
                ('is_top', models.BooleanField(default=False, verbose_name='producto_top')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Unit_Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='unidad_medida')),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidades de Medida',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='valor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('unit_measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.unit_measurement')),
            ],
            options={
                'verbose_name': 'Variante',
                'verbose_name_plural': 'Variantes',
                'ordering': ['product'],
            },
        ),
    ]

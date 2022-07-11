# Generated by Django 4.0.5 on 2022-07-11 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_rename_solicitudes_solicitud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID Producto')),
                ('nombreProducto', models.CharField(max_length=30, verbose_name='Nombre Producto')),
                ('imagen', models.CharField(max_length=256, null=True)),
                ('precio', models.IntegerField(verbose_name='Precio Producto')),
                ('stock', models.IntegerField(verbose_name='Stock Producto')),
            ],
        ),
    ]
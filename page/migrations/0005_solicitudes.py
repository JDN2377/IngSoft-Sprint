# Generated by Django 4.0.4 on 2022-07-02 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_rename_nombreareloj_reloj_nombrereloj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('idsolicitud', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de solicitud')),
                ('producto_solicitado', models.CharField(max_length=60, verbose_name='Producto solicitado')),
                ('cantidad_deseada', models.IntegerField(verbose_name='Cantidad deseada')),
            ],
        ),
    ]

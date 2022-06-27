# Generated by Django 4.0.5 on 2022-06-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('imagen_producto', models.CharField(max_length=150)),
                ('categoria_producto', models.CharField(max_length=50)),
                ('nombre_producto', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]

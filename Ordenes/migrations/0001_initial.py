# Generated by Django 4.1.3 on 2022-11-29 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agregaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=60)),
                ('faltantes', models.CharField(max_length=250)),
                ('producto', models.CharField(max_length=250)),
                ('serie', models.IntegerField()),
                ('cliente', models.CharField(max_length=100)),
                ('vendedor', models.CharField(max_length=60)),
                ('motivo', models.CharField(max_length=60)),
                ('cig', models.CharField(max_length=10)),
                ('observaciones', models.CharField(max_length=250)),
                ('saleSerie', models.IntegerField()),
                ('factura', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-29 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agregaitem',
            name='cig',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='agregaitem',
            name='cliente',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='agregaitem',
            name='estado',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='agregaitem',
            name='factura',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='agregaitem',
            name='faltantes',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='agregaitem',
            name='motivo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='agregaitem',
            name='observaciones',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='agregaitem',
            name='saleSerie',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agregaitem',
            name='serie',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agregaitem',
            name='vendedor',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]

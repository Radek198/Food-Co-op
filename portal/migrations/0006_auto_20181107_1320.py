# Generated by Django 2.1.3 on 2018-11-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20181106_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='suppliers',
        ),
        migrations.AddField(
            model_name='product',
            name='suppliers',
            field=models.ManyToManyField(null=True, to='portal.Supplier'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='photo',
            field=models.ImageField(max_length=225, null=True, upload_to=''),
        ),
    ]

# Generated by Django 2.1.3 on 2018-11-06 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20181106_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='photo',
            field=models.ImageField(blank=True, max_length=225, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='koop',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.Koop'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('spoldzielnia', '0004_auto_20180616_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residents',
            name='NIN',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]

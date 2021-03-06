# Generated by Django 2.0.6 on 2018-06-16 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('spoldzielnia', '0003_auto_20180614_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Residents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('NIN', models.CharField(max_length=15)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spoldzielnia.Flats')),
            ],
        ),
        migrations.AddField(
            model_name='payments',
            name='resident',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spoldzielnia.Residents'),
        ),
    ]

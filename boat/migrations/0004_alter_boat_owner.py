# Generated by Django 5.0 on 2023-12-09 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0003_boat_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boat.owner', verbose_name='Владелец'),
        ),
    ]

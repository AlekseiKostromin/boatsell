# Generated by Django 5.0 on 2023-12-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boathistory',
            options={'verbose_name': 'История', 'verbose_name_plural': 'История'},
        ),
        migrations.AlterField(
            model_name='boathistory',
            name='start_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Владел с'),
        ),
        migrations.AlterField(
            model_name='boathistory',
            name='stop_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Владел по'),
        ),
    ]

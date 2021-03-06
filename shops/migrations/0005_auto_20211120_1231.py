# Generated by Django 3.2.9 on 2021-11-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_product_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-price']},
        ),
        migrations.AddField(
            model_name='invoice',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Usunięty'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='Ukryty'),
        ),
    ]

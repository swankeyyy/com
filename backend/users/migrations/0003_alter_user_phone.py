# Generated by Django 4.2 on 2024-03-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_adress_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Номер телефона'),
        ),
    ]
# Generated by Django 3.2.5 on 2022-08-24 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuenta',
            options={'managed': False, 'verbose_name': 'cuenta', 'verbose_name_plural': 'cuentas'},
        ),
    ]
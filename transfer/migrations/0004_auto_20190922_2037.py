# Generated by Django 2.2.5 on 2019-09-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0003_auto_20190922_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='iso_code',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
# Generated by Django 2.1.3 on 2019-02-14 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactList', '0004_auto_20190213_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='latitude',
            field=models.DecimalField(decimal_places=5, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='longitutde',
            field=models.DecimalField(decimal_places=5, max_digits=8, null=True),
        ),
    ]

# Generated by Django 2.1.3 on 2019-02-13 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactList', '0002_auto_20181218_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='latitude',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='contact',
            name='longitutde',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
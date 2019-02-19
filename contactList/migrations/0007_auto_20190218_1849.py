# Generated by Django 2.1.3 on 2019-02-18 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactList', '0006_auto_20190213_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='latitude',
            field=models.DecimalField(decimal_places=5, editable=False, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='longitude',
            field=models.DecimalField(decimal_places=5, editable=False, max_digits=8, null=True),
        ),
    ]

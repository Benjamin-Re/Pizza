# Generated by Django 2.0.3 on 2019-11-04 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_toppingamount_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='toppingamount',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]

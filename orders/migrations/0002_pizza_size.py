# Generated by Django 2.0.3 on 2019-08-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('l', 'large'), ('s', 'small')], default='l', max_length=1),
        ),
    ]
# Generated by Django 2.2.6 on 2019-11-20 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='otp',
            field=models.IntegerField(default=None),
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-02 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
            ],
        ),
    ]

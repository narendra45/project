# Generated by Django 2.2.6 on 2019-11-09 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_merchant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.IntegerField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=100)),
                ('prod_price', models.FloatField()),
                ('prod_qty', models.IntegerField()),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Merchant')),
            ],
        ),
    ]

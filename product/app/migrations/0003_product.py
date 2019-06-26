# Generated by Django 2.1.4 on 2018-12-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181228_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_id', models.IntegerField()),
                ('l_product', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('l_price', models.IntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
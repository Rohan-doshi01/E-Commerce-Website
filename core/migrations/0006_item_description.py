# Generated by Django 3.1.2 on 2021-04-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test description. Any description related to the product can be inserted here'),
            preserve_default=False,
        ),
    ]
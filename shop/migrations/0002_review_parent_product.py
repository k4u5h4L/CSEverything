# Generated by Django 3.1.4 on 2020-12-06 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='parent_product',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
            preserve_default=False,
        ),
    ]
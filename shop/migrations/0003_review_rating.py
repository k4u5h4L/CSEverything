# Generated by Django 3.1.4 on 2020-12-06 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_review_parent_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[(1, '1 Star'), (2, '2 Star'), (3, '3 Star'), (4, '4 Star'), (5, '5 Star')], default=3, max_length=10),
            preserve_default=False,
        ),
    ]
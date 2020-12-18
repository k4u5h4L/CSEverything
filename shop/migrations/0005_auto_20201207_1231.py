# Generated by Django 3.1.4 on 2020-12-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201207_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[('SH', 'Shirts'), ('HO', 'Hoodies'), ('CF', 'Coffee Mugs'), ('PT', 'Pants'), ('SP', 'Sweat pants'), ('JK', 'Jackets'), ('CP', 'Caps'), ('TS', 'T-shirts')], max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[(1, '1 Star'), (2, '2 Star'), (3, '3 Star'), (4, '4 Star'), (5, '5 Star')], max_length=10),
        ),
    ]

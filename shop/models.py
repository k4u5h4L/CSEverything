from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from users.models import CustomUser
from django.db.models import Avg

# Create your models here.

CAT_CHOICES = [
    ('SH', 'Shirts'),
    ('HO', 'Hoodies'),
    ('CF', 'Coffee Mugs'),
    ('PT', 'Pants'),
    ('SP', 'Sweat pants'),
    ('JK', 'Jackets'),
    ('CP', 'Caps'),
    ('TS', 'T-shirts'),
]

RATING_CHOICES = [
    ('1', '1 Star'),
    ('2', '2 Star'),
    ('3', '3 Star'),
    ('4', '4 Star'),
    ('5', '5 Star'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.png', upload_to='product_pics')
    category = models.CharField(choices=CAT_CHOICES, max_length=50)

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=timezone.now)
    rating = models.CharField(choices=RATING_CHOICES, max_length=10)

    def __str__(self):
        return self.title

class Cart(models.Model):

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE)

    cart_items = models.ManyToManyField(Product)

    def __str__(self):
        return f'Cart of {self.user.username}'

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.defaults import page_not_found
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings

from .models import Product, Review
from . import models


# Create your views here.

@login_required
def shop_home_page(request):
    return render(request, 'shop/shop_home.html')

@login_required
def shop_product_page(request, productId):
    try:
        product = Product.objects.get(id=productId)
    except Product.DoesNotExist:
        raise Http404("No CustomUser matches the given query.")

    context = {
        'product': product,
    }
    for i in models.CAT_CHOICES:
        if i[0] == product.category:
            # PAIR_FOUND = True
            context['product_category'] = i[1]
            break

    reviews = product.review_set.all()
    context['reviews'] = reviews
    
    return render(request, 'shop/shop_product.html', context)

# @login_required
# def create_review(request):

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.defaults import page_not_found
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings

from .models import Product, Review
from . import models
from .forms import ReviewForm


# Create your views here.

def shop_home_page(request):
    products = Product.objects.all().order_by('-timestamp')

    context = {}

    context['products'] = []

    review_sum = 0

    for product in products:
        reviews = product.review_set.all()
        if len(reviews) != 0:
            review_sum = sum([int(review.rating) for review in reviews]) / len(reviews)
            review_sum = review_sum * 20
        else:
            review_sum = 0
        context['products'].append({'product': product, 'review_sum': review_sum, 'reviews': reviews})

    print(context['products'][0]['review_sum'])

    return render(request, 'shop/shop_home.html', context)

def shop_product_page(request, productId):
    try:
        product = Product.objects.get(id=productId)
    except Product.DoesNotExist:
        raise Http404("No CustomUser matches the given query.")

    review_form = ReviewForm()

    context = {
        'product': product,
        'form': review_form,
    }
    for i in models.CAT_CHOICES:
        if i[0] == product.category:
            # PAIR_FOUND = True
            context['product_category'] = i[1]
            break

    reviews = product.review_set.all()
    context['reviews'] = reviews
    if len(reviews) != 0:
        context['review_sum'] = sum([int(review.rating) for review in reviews]) / len(reviews)
        context['review_sum'] = context['review_sum'] * 20
    else:
        context['review_sum'] = 0
        
    return render(request, 'shop/shop_product.html', context)

def create_review(request, productId):
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=productId)
        except Product.DoesNotExist:
            raise Http404("No CustomUser matches the given query.")

        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.parent_product = product
            review.author = request.user

            review.save()
            print(f'Review created by user: {request.user.username}!')
            return redirect('shop_product_page', productId)

        else:
            print(f'form was not valid')
            print(form.errors)
            return redirect('shop_product_page', productId)

    else:
        print('GET request')
        return redirect('shop_product_page', productId)

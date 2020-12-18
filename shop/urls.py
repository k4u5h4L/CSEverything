from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop_home_page, name='shop_home_page'),
    path('create/review/<int:productId>/', views.create_review, name='create_review_page'),
    path('product/<int:productId>/', views.shop_product_page, name='shop_product_page'),
]
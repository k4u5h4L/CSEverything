from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop_home_page, name='shop_home_page'),
    path('product/<int:productId>/', views.shop_product_page, name='shop_product_page'),
]
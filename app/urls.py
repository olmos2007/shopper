
from django.urls import path, include
from app.views.register import register, login
from app.views.index import index, product_details, shop_view, shopping_cart, checkout, contact,\
    create_product,update_product, delete_product



urlpatterns = [
    path('', index, name='index'),
    path('product-details/<int:product_id>', product_details, name='shop-details'),
    path('shop/', shop_view, name='shop'),
    path('shopping-cart/', shopping_cart, name='shopping-cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),

    path('create-product/', create_product, name='create-product'),
    path('update-product/<int:product_id>', update_product, name='update-product'),
    path('delete-product/<int:product_id>', delete_product, name='delete-product'),

    path('register/', register, name='register'),
    path('login/', login, name='login'),
]

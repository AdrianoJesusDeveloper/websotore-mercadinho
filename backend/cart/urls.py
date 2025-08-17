from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('remove/', views.remove_from_cart, name='remove_from_cart'),
    path('view/', views.cart_detail, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('cart/', views.cart_detail, name="cart"),
    path('add/<int:plant_id>/', views.cart_add, name="cart_add"),
    path('remove/<int:plant_id>/', views.cart_remove, name="cart_remove"),
    path('checkout/', views.checkout, name="checkout"),
    path('update/', views.cart_update, name='cart_update'),

] 
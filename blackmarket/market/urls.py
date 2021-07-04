from django.urls import path
from . import views
from .views import UserRegisterView

urlpatterns = [

    path('', views.main, name="main"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('market/', views.market, name="market"),
    path('register/', UserRegisterView.as_view(), name='register'),
]

from django.urls import path
from . import views
from .views import UserRegisterView, CreateProduct, UpdateProduct, DetailProduct, DeleteProduct, ProductList, DetailProfile

urlpatterns = [

    path('', views.main, name="main"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('market/', ProductList.as_view(), name="market"),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('market/create', CreateProduct.as_view(),  name='create_product'),
    path('market/<int:pk>', DetailProduct.as_view(),  name='detail_product'),
    path('market/<int:pk>/update', UpdateProduct.as_view(),  name='update_product'),
    path('market/<int:pk>/delete', DeleteProduct.as_view(),  name='delete_product'),
    path('profile/<int:pk>', DetailProfile.as_view(),  name='detail_profile'),
]

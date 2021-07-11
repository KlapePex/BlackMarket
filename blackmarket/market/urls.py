from django.urls import path
from . import views
from .views import UserRegisterView, CreateProduct, UpdateProduct, DetailProduct, DeleteProduct, ProductList, \
    DetailProfile, CarsList, ElectronicsList, GunsList, MeleeList, NaturalDrugsList, SyntheticDrugsList

urlpatterns = [

    path('', views.main, name='main'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('market/', ProductList.as_view(), name='market'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('market/create', CreateProduct.as_view(),  name='create_product'),
    path('market/<int:pk>', DetailProduct.as_view(),  name='detail_product'),
    path('market/<int:pk>/update', UpdateProduct.as_view(),  name='update_product'),
    path('market/<int:pk>/delete', DeleteProduct.as_view(),  name='delete_product'),
    path('profile/<int:pk>', DetailProfile.as_view(),  name='detail_profile'),
    path('cars/', CarsList.as_view(), name='cars'),
    path('electronics/', ElectronicsList.as_view(), name='electronics'),
    path('guns/', GunsList.as_view(), name='guns'),
    path('melee/', MeleeList.as_view(), name='melee'),
    path('natural_drugs/', NaturalDrugsList.as_view(), name='natural_drugs'),
    path('synthetic_drugs/', SyntheticDrugsList.as_view(), name='synthetic_drugs'),
    path('update_item/', views.update_item, name="update_item")
]

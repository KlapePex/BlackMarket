from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import RegistrationForm
from .models import Product, Profile, Order, OrderItem, ShippingAddress
from django.contrib.auth.mixins import PermissionRequiredMixin
from . utils import cartData, cookieCart, guestOrder
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime
import json
from django.db.models import Q


class UserRegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class DeleteProduct(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_product.html'
    model = Product
    context_object_name = 'products'
    success_url = reverse_lazy('market')
    permission_required = 'market.delete_product'


class ProductList(ListView):
    template_name = 'market/market.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):

        search = self.request.GET.get('search', None)

        if search:
            queryset = Product.objects.filter(Q(name__contains=search) | Q(category__contains=search))
        else:
            queryset = Product.objects.all()

        return queryset


def main(request):
    context = {}
    return render(request, 'market/main.html', context)


class CreateProduct(PermissionRequiredMixin, CreateView):
    template_name = 'market/create_product.html'
    model = Product
    success_url = reverse_lazy('market')
    fields = '__all__'
    permission_required = 'market.add_product'


class DetailProduct(DetailView):
    template_name = 'market/detail_product.html'
    model = Product
    context_object_name = 'product'


class UpdateProduct(PermissionRequiredMixin, UpdateView):
    template_name = 'market/update_product.html'
    model = Product
    success_url = reverse_lazy('market')
    fields = '__all__'
    context_object_name = 'product'
    permission_required = 'market.change_product'
    

class DetailProfile(DetailView):
    template_name = 'market/detail_profile.html'
    model = Profile
    context_object_name = 'profile'


class CarsList(ListView):
    template_name = 'categories/cars.html'
    model = Product
    context_object_name = 'products'


class ElectronicsList(ListView):
    template_name = 'categories/electronics.html'
    model = Product
    context_object_name = 'products'


class GunsList(ListView):
    template_name = 'categories/guns.html'
    model = Product
    context_object_name = 'products'


class MeleeList(ListView):
    template_name = 'categories/melee.html'
    model = Product
    context_object_name = 'products'


class NaturalDrugsList(ListView):
    template_name = 'categories/natural_drugs.html'
    model = Product
    context_object_name = 'products'


class SyntheticDrugsList(ListView):
    template_name = 'categories/synthetic_drugs.html'
    model = Product
    context_object_name = 'products'


def cart(request):

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        order = []
        items = []
        customer = []
    context = {"items": items, "order": order, "customer": customer}
    return render(request, 'market/cart.html', context)


def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', product_id)

    customer = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)


def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'market/checkout.html', context)


@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            county=data['shipping']['county'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete!', safe=False)

from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import Product, Category, Profile
from django.contrib.auth.mixins import PermissionRequiredMixin
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

def cart(request):
    context = {}
    return render(request, 'market/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'market/checkout.html', context)


class ProductList(ListView):
    template_name = 'market/market.html'
    model = Product
    context_object_name = 'products'
    def get_queryset(self):

        search = self.request.GET.get('search', None)

        if search:
            queryset = Product.objects.filter(Q(name__contains=search) | Q(category__title__contains=search))
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
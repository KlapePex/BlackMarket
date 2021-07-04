from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm


class UserRegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def cart(request):
    context = {}
    return render(request, 'market/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'market/checkout.html', context)


def market(request):
    context = {}
    return render(request, 'market/checkout.html', context)


def main(request):
    context = {}
    return render(request, 'market/main.html', context)

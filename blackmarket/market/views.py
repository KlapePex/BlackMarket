from django.shortcuts import render

# Create your views here.
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
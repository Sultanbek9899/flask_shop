from django.shortcuts import render,get_object_or_404, redirect

from django.views.generic import TemplateView 
# Create your views here.

from src.apps.product.models import Product, Category
from src.apps.cart.cart import Cart



def add_cart(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product,id=pk)
    cart.add(product)
    return redirect("index")

def remove_from_cart(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, id=pk)
    cart.remove(product)
    return redirect("cart_detail")


class CartTemplateView(TemplateView):
    template_name = "cart.html"



def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")
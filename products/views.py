from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Offer

# Create your views here.


def index(request):
    products = Products.objects.all()
    offer = Offer.objects.all()
    return render(request, 'index.html',
                  {'products': products}, {'offer': offer})


def new(request):
    return HttpResponse("These are the new products")

from django.shortcuts import render

# Create your views here.
from app.models import Wheel, Nav, Mustbuy, Shop


def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuy = Mustbuy.objects.all()
    shops = Shop.objects.all()

    shophead = shops[0]
    shoptab = shops[1:3]
    shopclass_list = shops[3:7]
    shopcommend = shops[7:11]


    response_dir = {
        'wheels':wheels,
        'navs': navs,
        'mustbuy': mustbuy,
        'shophead': shophead,
        'shoptab': shoptab,
        'shopclass_list': shopclass_list,
        'shopcommend': shopcommend,
    }

    return render(request,'home/home.html',context=response_dir)


def market(request):
    return render(request,'market/market.html')


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')
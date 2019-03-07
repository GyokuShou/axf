from django.shortcuts import render

# Create your views here.
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtype, Goods


def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuy = Mustbuy.objects.all()
    shops = Shop.objects.all()

    shophead = shops[0]
    shoptab = shops[1:3]
    shopclass_list = shops[3:7]
    shopcommend = shops[7:11]
    mainshows = MainShow.objects.all()

    response_dir = {
        'wheels':wheels,
        'navs': navs,
        'mustbuy': mustbuy,
        'shophead': shophead,
        'shoptab': shoptab,
        'shopclass_list': shopclass_list,
        'shopcommend': shopcommend,
        'mainshows': mainshows,
    }

    return render(request,'home/home.html',context=response_dir)


def market(request,id=1):
    page = request.COOKIES.get('page')
    if page == None:
        page = id
    foodtypes = Foodtype.objects.all()
    type_no = foodtypes.filter(id=page).first()
    type_no = type_no.typeid
    good_list = Goods.objects.filter(categoryid=type_no)
    response_dir = {
        'foodtypes': foodtypes,
        'good_list': good_list,
        'page': page,
    }

    response = render(request,'market/market.html', context=response_dir)
    response.set_cookie('page',id)
    return response


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')
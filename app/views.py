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


def market(request,childcid='0',sortid='0'):
    page = int(request.COOKIES.get('page', '0'))
    foodtypes = Foodtype.objects.all()
    categoryid = foodtypes[page].typeid
    good_list = Goods.objects.filter(categoryid=categoryid)

    if childcid != '0':
        good_list = good_list.filter(childcid=childcid)

    if sortid == '1':
        good_list = good_list.order_by('-productnum')
    elif sortid == '2':
        good_list = good_list.order_by('price')
    elif sortid == '3':
        good_list = good_list.order_by('-price')


    childtypenames = foodtypes[page].childtypenames
    childtype_list = []
    for item in childtypenames.split('#'):
        item_arr = item.split(':')
        temp_dir = {
            'name': item_arr[0],
            'id': item_arr[1]
        }
        childtype_list.append(temp_dir)

    response_dir = {
        'foodtypes': foodtypes,
        'good_list': good_list,
        'childtype_list': childtype_list,
        'childcid': childcid,
    }

    response = render(request,'market/market.html', context=response_dir)
    return response


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')
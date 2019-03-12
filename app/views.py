import hashlib
import random
import time

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtype, Goods, User, Cart, Order, OrderGoods


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

    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.filter(pk=userid).first()
        cart = user.cart_set.all()
        response_dir['carts'] = cart

    response = render(request,'market/market.html', context=response_dir)
    return response


def cart(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)

    carts = user.cart_set.filter(number__gt=0)

    isall = True
    for cart in carts:
        if not cart.isselect:
            isall = False

    response_data = {
        'carts': carts,
        'isall': isall,
    }
    return render(request,'cart/cart.html',context=response_data)


def mine(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    if userid:
        user = User.objects.get(pk=userid)

    return render(request,'mine/mine.html',context={'user':user})


def login(request):
    if request.method == 'GET':
        return render(request,'mine/login.html')
    elif request.method == 'POST':
        back = request.COOKIES.get('back')
        email = request.POST.get('email')
        password = generate_password(request.POST.get('password'))
        user = User.objects.filter(email=email).filter(password=password)
        if user.exists():
            user = user.first()
            token = generate_token()
            cache.set(token,user.id,60*60*24*3)
            request.session['token'] = token
            # return render(request,'mine/mine.html',context={'user':user})
            if back == 'mine':
                return redirect('app:mine')
            else:
                return redirect('app:marketbase')
            # return redirect('app:mine')
        else:
            return render(request,'mine/login.html',context={'error':'用户名或密码错误'})


def logout(request):
    request.session.flush()
    return redirect('app:mine')


def generate_password(param):
    sha1 = hashlib.sha1()
    sha1.update(param.encode('utf-8'))
    return sha1.hexdigest()


def generate_token():
    token = str(time.time()) + str(random.random())
    ps = hashlib.sha1()
    ps.update(token.encode('utf-8'))
    return ps.hexdigest()


def register(request):
    if request.method == 'GET':
        return render(request, 'mine/register.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = generate_password(request.POST.get('password'))

        try:
            user = User()
            user.email = email
            user.name = name
            user.password = password
            user.save()

            token = generate_token()
            cache.set(token, user.id, 60 * 60 * 24 * 3)
            request.session['token']=token
            return redirect('app:mine')
        except Exception as e:
            return render(request,'mine/register.html')


def checkemail(request):
    email = request.GET.get('email')
    user = User.objects.filter(email=email)
    response_data = {}
    if user.exists():
        response_data['status'] = False
        response_data['msg'] = '该账户已被占用'
    else:
        response_data['status'] = True
        response_data['msg'] = '该用户名可用'
    return JsonResponse(response_data)


def addcart(request):
    token = request.session.get('token')
    response_data = {}
    if token:
        userid = cache.get(token)
        user = User.objects.filter(pk=userid)
        if user.exists():
            user = user.first()
            goodsid = request.GET.get('goodsid')
            good = Goods.objects.filter(pk=goodsid).first()
            cart = Cart.objects.filter(user=user).filter(goods=good)
            if cart.exists():
                cart = cart.first()
                cart.number += 1
                cart.save()
            else:
                cart = Cart()
                cart.user = user
                cart.goods = good
                cart.number = 1
                cart.save()
            response_data['status'] = 1
            response_data['num'] = cart.number
            return JsonResponse(response_data)

    response_data['status'] = -1
    return JsonResponse(response_data)


def subcart(request):
    goodsid = request.GET.get('goodsid')
    response_data = {}
    goods = Goods.objects.get(pk=goodsid)
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)

    cart = Cart.objects.filter(user=user).filter(goods=goods).first()
    cart.number -= 1
    cart.save()
    response_data['status']=1
    response_data['num'] = cart.number
    return JsonResponse(response_data)


def changecartselect(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()

    response_data = {
        'status': 1,
        'isselect': cart.isselect,
    }
    return JsonResponse(response_data)


def changecartall(request):
    isall = request.GET.get('isall')

    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    carts = user.cart_set.all()

    if isall == 'true':
        isall = True
    else:
        isall = False

    for cart in carts:
        cart.isselect = 1
        cart.save()

    response_data = {
        'status': 1,
    }

    return JsonResponse(response_data)


def generate_identifier():
    tmp = str(time.time()) + str(random.randrange(1000,10000))
    return tmp


def generateorder(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)

    order = Order()
    order.user = user
    order.identifier = generate_identifier()
    order.save()

    carts = user.cart_set.filter(isselect=True)
    for cart in carts:
        order_goods = OrderGoods()
        order_goods.goods = cart.goods
        order_goods.order = order
        order_goods.number = cart.number
        order_goods.save()

        cart.delete()

    # response_data = {
    #     'status': 1,
    #     'identifier': order.identifier
    # }


    return render(request,'order/orderdetail.html',context={'order':order})
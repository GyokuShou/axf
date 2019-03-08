from django.db import models

# Create your models here.

# img,name,trackid

class BaseModel(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

# 轮播图
class Wheel(BaseModel):
    class Meta:
        db_table = 'axf_wheel'

# 导航
class Nav(BaseModel):
    class Meta:
        db_table = 'axf_nav'

# 每日必购
class Mustbuy(BaseModel):
    class Meta:
        db_table = 'axf_mustbuy'

class Shop(BaseModel):
    class Meta:
        db_table = 'axf_shop'


class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=100)
    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)
    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)
    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_mainshow'

# typeid,typename,childtypenames,typesort
class Foodtype(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'

class Goods(models.Model):
    productid = models.CharField(max_length=10)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)
    isxf = models.BooleanField(default=False)
    pmdesc = models.BooleanField(default=False)
    specifics = models.CharField(max_length=100)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.CharField(max_length=10)
    childcid = models.CharField(max_length=10)
    childcidname = models.CharField(max_length=50)
    dealerid = models.CharField(max_length=10)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'

class User(models.Model):
    email = models.CharField(max_length=40,unique=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=40,default='axf.png')
    rank = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_user'
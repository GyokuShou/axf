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
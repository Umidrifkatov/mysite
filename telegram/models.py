from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from . import views
import os


class TgUser(models.Model):
    userid = models.IntegerField(unique=True, verbose_name='id пользователя')
    phone = models.CharField(max_length=12, null=True, verbose_name='телефон')
    name = models.CharField(max_length=100, null=True, verbose_name='имя')
    lang = models.CharField(max_length=2, null=True, verbose_name='язык')
    location = models.CharField(max_length=100, null=True, verbose_name='местоположение')
    step = models.IntegerField(default=0, null=True, verbose_name='шаг')
    payment = models.CharField(max_length=100, null=True, verbose_name='способ оплаты')
    delivery = models.BooleanField(default=True, verbose_name='доставка')
    deferred = models.BooleanField(default=False, verbose_name='отложенный')
    messageid = models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        
    
    

class Category(models.Model):
    name = models.CharField(max_length=23, verbose_name='название')
    active = models.BooleanField(default=True, verbose_name='активен')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=u'надкатегория')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
    
    
class Product(models.Model):
    name = models.CharField(max_length=23, verbose_name='название')
    caption = models.TextField(max_length=1044, verbose_name='описание')
    price = models.IntegerField(verbose_name='цена')
    pic = models.ImageField(upload_to='bot/', null=True, blank=True, verbose_name='изображение', help_text="БЕЗ ИЗОБРАЖЕНИЯ НЕАКТИВЕН")
    photo = models.CharField(max_length=1024, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='категория')
    active = models.BooleanField(default=True, verbose_name='активен')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'
    
@receiver(pre_save, sender=Product)
def photosendesaver(sender, instance, *args, **kwargs):
    if instance.pic:
        instance.photo = views.tgfileid(instance.pic)
        instance.pic = None
    elif instance.photo == None and not instance.photo:
        instance.active = False
        
    

class Cart(models.Model):
    user = models.ForeignKey(TgUser, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField(default=1)
    status = models.BooleanField(default=False)
    
    
    
class Order(models.Model):
    user = models.ForeignKey(TgUser, on_delete=models.SET_NULL, null=True, verbose_name='пользователь')
    itemandcost = models.TextField(max_length=2096, default=None, verbose_name='товары')
    withmarkup = models.CharField(max_length=2096, default=None, null=True)
    time = models.DateTimeField(auto_now_add=True, verbose_name='время заказа')
    total = models.CharField(max_length=101, verbose_name='сумма')
    geo = models.CharField(max_length=100, null=True, verbose_name='локация')
    deliver = models.BooleanField(default=False, null=True, verbose_name='доставка')
    deferred = models.BooleanField(default=False, null=True, verbose_name='отложенный')
    messageid = models.IntegerField(null=True)
    status = models.CharField(max_length=100, verbose_name='состояние')
    
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'
    
    
class StatDay(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='день')
    doneorders = models.IntegerField(null=True, verbose_name='всего в день')
    daysum = models.IntegerField(null=True, verbose_name='сумма в день')
    
    class Meta:
        verbose_name = 'статистика'
        verbose_name_plural = 'статистика за день'
        
class StatWeek(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата')
    doneorders = models.IntegerField(null=True, verbose_name='всего заказов')
    weeksum = models.IntegerField(null=True, verbose_name='недельная сумма')
    
    class Meta:
        verbose_name = 'статистика'
        verbose_name_plural = 'статистика за неделю'
        
class MonthStat(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата')
    doneorders = models.IntegerField(null=True, verbose_name='всего заказов')
    monthsum = models.IntegerField(null=True, verbose_name='месячная сумма')
    
    class Meta:
        verbose_name = 'статистика'
        verbose_name_plural = 'статистика за месяц'



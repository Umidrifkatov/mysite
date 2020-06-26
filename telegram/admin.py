from django.contrib import admin
from .models import TgUser, Category, Product, Cart, Order, StatDay, StatWeek, MonthStat



class TgUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'userid', 'phone', 'lang' )
admin.site.register(TgUser, TgUserAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parEnt','active')
    list_editable = ('active',)
    list_filter = ('active', 'name',)
    
    def parEnt(self, obj):
        try:
            return obj.parent.name
            
        except Exception:
            return 'Нет'
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'caption','catEgory','active',)
    list_editable = ('active',)
    # list_filter = ('active', 'name',)
    fields = ('name', 'caption', 'price', 'active', 'pic', 'category',)
    
    
    def catEgory(self, obj):
        try:
            return obj.category.name
            
        except Exception:
            return 'нет родительской'

admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('get_product','get_user','qty','status',)
    def get_user(self, obj):
        return obj.user.userid
    def get_product(self, obj):
        return obj.product.name
    
admin.site.register(Cart, CartAdmin)
    


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'time','usErname','usErphone', 'total', 'status')
    list_filter = ('status',)
    list_display_links = ('id', 'time')
    list_per_page = 15
    def getid(self, obj):
        return obj.id
    def usErphone(self, obj):
        return obj.user.phone
    def usErname(self, obj):
        return obj.user.name

admin.site.register(Order, OrderAdmin)


class DaystatAdmin(admin.ModelAdmin):
    list_display = ('date', 'doneorders', 'daysum',)
admin.site.register(StatDay, DaystatAdmin)

class WeekStatAdmin(admin.ModelAdmin):
    list_display = ('date', 'doneorders', 'weeksum',)
admin.site.register(StatWeek, WeekStatAdmin)

class MonthStatA(admin.ModelAdmin):
    list_display = ('date', 'doneorders', 'monthsum',)
admin.site.register(MonthStat, MonthStatA)
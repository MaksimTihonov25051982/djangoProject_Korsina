from django.contrib import admin
from .models import *
# Register your models here.
class adminTovar(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'categoru')

admin.site.register(Tovar, adminTovar)

class adminKorzina(admin.ModelAdmin):
    list_display = ('summa', 'user')

admin.site.register(Korzina, adminKorzina)

class adminOrder(admin.ModelAdmin):
    list_display = ('user', 'status', 'adres')

admin.site.register(Order, adminOrder)


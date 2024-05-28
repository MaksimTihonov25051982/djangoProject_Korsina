import telebot
from django.shortcuts import render, redirect
from .models import *
from .form import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


from  django.contrib.auth.forms import UserCreationForm # библиотека для формы
# Create your views here.
def index(reguest):
    # telegram()
    return render(reguest, 'index.html')

def goods(reguest, cat):
    items = Tovar.objects.filter(categoru=cat)
    print(items)
    data = {'items':items, 'cat':cat}
    return render(reguest, 'goods.html', data)

def buy(reguest, itemid, cat):
    item = Tovar.objects.get(id=itemid)
    print(item)
    userid = reguest.user.id
    if Korzina.objects.filter(user_id=userid, tovar_id=itemid):
        item = Korzina.objects.get(tovar_id=itemid)
        item.count += 1
        item.summa = item.calSumma()
        item.save()
    else:
        Korzina.objects.create(count=1, tovar_id=itemid, user_id=userid,
                               summa=item.price)
    return redirect('goods',cat)


    ################    Корзина    ###################
def cart(reguest):
    forma = FormOrder
    mykorzina = Korzina.objects.filter(user_id=reguest.user.id)
    print(mykorzina.values())
    q = list()
    for i in mykorzina:
        item = i.tovar
        q.append(item)
    print(q)

    total = 0
    sps = ''
    for one in mykorzina:
        total += one.summa

    if reguest.POST:
        print(1)
        forma = FormOrder(reguest.POST)
        if forma.is_valid():
            print('Ok.')
            k1 = forma.cleaned_data.get('adres')
            k2 = forma.cleaned_data.get('telefon')
            print(k1, k2)
            zakaz = ''
            for one in mykorzina:
               zakaz += one.tovar.name+ ''+str(one.count)+\
                        ''+str(one.summa)+'\n'
            zakaz += 'Всего: ' + str(total) + '\n'
            zakaz+= 'Адрес: ' +k1+'\n'
            zakaz += 'Телефон: ' + k2
            curOrder = Order.objects.create(adres=k1,  telefon=k2, zakaz=zakaz,
                                 status='в сборке', user=reguest.user,
                                 total=total)

            for one in mykorzina:
                print(one.tovar)
                print(curOrder)
                curOrder.items.add(one.tovar)
            curOrder.save()


            mykorzina.delete() # удаление
            total = 0
            forma = FormOrder()
            sps = 'Спасибо за заказ !!!'
            telegram(zakaz)
    data = {'items': mykorzina, 'total': total,
            'formaorder': forma, 'sps':sps}

    return render(reguest, 'cart.html', data)

# Удаление из корзины
def delete(reguest, itemid):
    item = Korzina.objects.get(id=itemid)
    item.delete()
    return  redirect('cart')

# '+','-' в корзине
def edit(reguest,itemid,num):
    num = int(num)
    item = Korzina.objects.get(id=itemid)
    item.count += num
    item.summa = item.calSumma()
    if item.count>0:
        item.save()
    return  redirect('cart')
    #################################################


    ######## Фуккция для регистрации на сайте########

def registr(reguest):
    # forma = UserCreationForm
    print(1)
    if reguest.POST:
        print(2)
        forma = formaRegistr(reguest.POST) # форма для регистрации
        if forma.is_valid():  # проверка пройдена
            print(3)
            # собираем данные
            y1 = forma.cleaned_data.get('username')
            y2 = forma.cleaned_data.get('password')
            y3 = forma.cleaned_data.get('email')
            y4 = forma.cleaned_data.get('first_name')
            y5 = forma.cleaned_data.get('last_name')
            User.objects.create_user(username=y1, password=y2) # добавляем новую строку в таблице
            user = User.objects.get(username=y1) # находим пользователя
            # заполняем данные
            user.email = y3
            user.first_name = y4
            user.last_name = y5

            user.save()  # сохраняем данные
            login(reguest,user)  # вход пользователя на сайт
            return redirect('home')  # на главную
    else:
        forma = formaRegistr()
    data = {'form':forma}
    return render(reguest,'registration/registration.html', data)

def cabinet(reguest):
    user = reguest.user
    items = Order.objects.filter(user=user)
    data = {'items':items}
    return render(reguest, 'cabinet.html', data)

    #########################################


def telegram(message):
    #t.me/Tetetris2024bot.
    token = '7150763462:AAFXyQV2_pWINj8L5dWD2XPoEmnxXh331Mk'
    chat = 829581272
    import telebot

    bot = telebot.TeleBot(token)
    bot.send_message(chat, message)

def myzakaz(reguest,itemid):
    item = Order.objects.get(id=itemid)
    data = {'item':item}
    return render(reguest,'myzakaz.html',data)

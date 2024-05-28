"""
URL configuration for djangoProject_Korsina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from appcorzina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'home'),
    path('goods/<str:cat>/', views.goods, name='goods'),
    path('goots/buy/<int:itemid>/<str:cat>/', views.buy, name='buy'),
    path('cart/', views.cart, name='cart'),

    # Регистрация на сайте
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', views.registr, name='registr'),
    path('accounts/login', views.index),
    path('cabinet/', views.cabinet, name='cabinet'),
    #################################################

    # Удаление из корзины
    path('cart/delete/<int:itemid>/', views.delete, name='delete'),

    # "+" в корзину
    path('cart/edit/<int:itemid>/<str:num>', views.edit, name='edit'),

    path('myzakaz/<int:itemid>', views.myzakaz, name='myzakaz'),
]

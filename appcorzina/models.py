from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tovar(models.Model):
    STAT = (('П', 'Продукты'),('Л', 'Лекарства'),('О', 'Одежда'),('По', 'Посуда'))
    name = models.CharField(max_length=100, verbose_name='Название.')
    price = models.IntegerField(verbose_name='Цена.')
    image = models.FileField(verbose_name='Изображение.',
                             upload_to='img/',
                             blank=True, null=True)
    discount = models.IntegerField(verbose_name='Скидка',
                             default=0)
    categoru = models.CharField(choices=STAT, max_length=100,
                             blank=True, null=True)

    def __str__(self):
        return self.name

class Korzina(models.Model):
    tovar = models.ForeignKey(to=Tovar, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Колличество.')
    summa = models.DecimalField(verbose_name='Сумма.',
                                max_digits=8,
                                decimal_places=2)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def calSumma(self):
        return self.count * (self.tovar.price - self.tovar.discount/100 * self.tovar.price)

class Order(models.Model):
    STAT = (('В сборке.','В сборке.'), ('В пути.','В пути.'),('Доставлен.','Доставлен.'))
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    adres = models.CharField(max_length=100, verbose_name='Адрес')
    telefon = models.CharField(max_length=100, verbose_name='Телефон')
    items = models.ManyToManyField(to=Tovar, null=True, blank=True)
    zakaz = models.TextField(verbose_name='Заказ.')
    status = models.CharField(choices=STAT, max_length=100)
    total = models.DecimalField(verbose_name='Итог',
                                max_digits=8,
                                decimal_places=2, blank=True, null=True)
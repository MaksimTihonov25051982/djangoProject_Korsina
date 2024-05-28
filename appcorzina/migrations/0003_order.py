# Generated by Django 5.0.6 on 2024-05-16 12:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcorzina', '0002_alter_tovar_discount_alter_tovar_price_korzina'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres', models.CharField(max_length=100, verbose_name='Адрес')),
                ('telefon', models.CharField(max_length=100, verbose_name='Телефон')),
                ('zakaz', models.TextField(verbose_name='Заказ.')),
                ('status', models.CharField(choices=[(1, 'В сборке.'), (2, 'В пути.'), (3, 'Доставлен.')], max_length=100)),
                ('items', models.ManyToManyField(to='appcorzina.tovar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

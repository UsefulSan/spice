from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True)


class CurrencyMixin(models.Model):
    class Meta:
        abstract = True

    time = models.DateTimeField(verbose_name="Дата фрейма")
    open = models.FloatField(verbose_name="Цена открытия")
    high = models.FloatField(verbose_name='Максимум торгового диапазона')
    low = models.FloatField(verbose_name='Минимум торгового диапазона')
    close = models.FloatField(verbose_name="Цена закрытия")
    tick_volume = models.IntegerField()
    spred = models.IntegerField(verbose_name="Спред", null=True)
    real_volume = models.IntegerField()


class EURUSD_H1(CurrencyMixin):
    pass


class EURUSD_D1(CurrencyMixin):
    pass

# timeframes = {'m5', 'm10', 'm15', 'm30', 'h1', 'h4', 'd1', 'w1', 'mn1'}
# tickers = {'EURUSD', 'GBPUSD'}
# for timeframe in timeframes:
#     for ticket in tickers:
# class CUR_EURUSD_H1(CurrencyMixin):
#     pass


# model = f'{ticket}_{timeframe}'
# EURUSD_H1.__class__.__name__ = model
# print(model)


# def class_name_changer(cls):
#     for timeframe in timeframes:
#         for ticket in tickers:
#             cls.__name__ = f'{ticket}_{timeframe}'
#             print(cls.__name__)
#
# class_name_changer(EURUSD_H1)

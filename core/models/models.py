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

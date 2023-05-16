# Generated by Django 4.2.1 on 2023-05-16 07:45

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EURUSD_D1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EURUSD_H1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EURUSD_H4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EURUSD_M1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EURUSD_M15',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EURUSD_M30',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EURUSD_M5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EURUSD_W1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GBPUSD_D1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GBPUSD_H1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GBPUSD_H4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GBPUSD_M1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GBPUSD_M15',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GBPUSD_M30',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GBPUSD_M5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GBPUSD_W1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDCAD_D1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDCAD_H1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDCAD_H4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDCAD_M1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDCAD_M15',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDCAD_M30',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDCAD_M5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDCAD_W1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDJPY_D1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDJPY_H1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDJPY_H4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDJPY_M1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDJPY_M15',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDJPY_M30',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDJPY_M5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='USDJPY_W1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата фрейма')),
                ('open', models.FloatField(verbose_name='Цена открытия')),
                ('high', models.FloatField(verbose_name='Максимум торгового диапазона')),
                ('low', models.FloatField(verbose_name='Минимум торгового диапазона')),
                ('close', models.FloatField(verbose_name='Цена закрытия')),
                ('tick_volume', models.IntegerField()),
                ('spred', models.IntegerField(null=True, verbose_name='Спред')),
                ('real_volume', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

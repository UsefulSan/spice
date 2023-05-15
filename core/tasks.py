import datetime
import os

import MetaTrader5 as mt5
import pandas as pd
from celery import shared_task

from core.scripts.get_currency_data import SharesDataLoader
from core.scripts.main_value_currency import currency
from spice.settings import env

pd.set_option('display.max_columns', 500)  # сколько столбцов показываем
pd.set_option('display.width', 1500)  # макс. ширина таблицы для показа




@shared_task(name="checking_currency")
def checking_currency():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    how_many_bars = 100

    utc_till = datetime.datetime.now() + datetime.timedelta(days=1)  # получим данные по завтрашний день
    # utc_till = datetime.datetime.now() - datetime.timedelta(days=1)  # получим данные по вчерашний день
    print(utc_till)

    timeframes = {mt5.TIMEFRAME_M5, mt5.TIMEFRAME_M10, mt5.TIMEFRAME_M15, mt5.TIMEFRAME_M30, mt5.TIMEFRAME_H1,
                  mt5.TIMEFRAME_H4, mt5.TIMEFRAME_D1, mt5.TIMEFRAME_W1, mt5.TIMEFRAME_MN1}
    tickers = {'EURUSDrfd', 'GBPUSDrfd', 'USDJPYrfd', 'USDCADrfd'}

    for timeframe in currency.timeframe.values():
        for ticket in currency.tickers:
            load_data = SharesDataLoader(ticket)
            load_data.connect_to_metatrader5(path='C:\Program Files\MetaTrader 5 Alfa-Forex\terminal64.exe')
            load_data.connect_to_db(host=env("DB_HOST"),
                                    user=env("DB_USER"),
                                    password=env("DB_PASSWORD"),
                                    dbname=env("DB_NAME"))
            data = load_data.get_share_data(ticket=ticket, timeframe=timeframe[0], utc_till=utc_till,
                                            how_many_bars=how_many_bars)
            print(data)

            load_data.always_get_share_data(ticket=ticket, timeframe=timeframe[0])

            # load_data.disconnect_from_metatrader5()


checking_currency()

import datetime
import os

import MetaTrader5 as mt5
import pandas as pd
from celery import shared_task

from core.scripts.get_currency_data import SharesDataLoader
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

    # timeframes = {mt5.TIMEFRAME_M5, mt5.TIMEFRAME_M10, mt5.TIMEFRAME_M15, mt5.TIMEFRAME_M30, mt5.TIMEFRAME_H1,
    #                mt5.TIMEFRAME_H4, mt5.TIMEFRAME_D1, mt5.TIMEFRAME_W1, mt5.TIMEFRAME_MN1}
    timeframes = {mt5.TIMEFRAME_D1}
    tickers = {'EURUSDrfd'}  # , 'EURUSD', 'GBPUSD'

    for timeframe in timeframes:
        for ticket in tickers:
            load_data = SharesDataLoader(ticket)
            load_data.connect_to_metatrader5(path='C:\Program Files\MetaTrader 5 Alfa-Forex\terminal64.exe')
            load_data.connect_to_db(host=env("DB_HOST"),
                                    user=env("DB_USER"),
                                    password=env("DB_PASSWORD"),
                                    dbname=env("DB_NAME"))
            data = load_data.get_share_data(ticket=ticket, timeframe=timeframe, utc_till=utc_till,
                                            how_many_bars=how_many_bars)
            print(data)

            # how_many_bars = 10
            # data = load_data.get_share_data_from_db(ticket="SBER", timeframe=mt5.TIMEFRAME_D1, how_many_bars=how_many_bars)
            # print(data)

            load_data.always_get_share_data(ticket=ticket, timeframe=timeframe)
            # load_data.export_to_csv(ticket=ticket, timeframe=timeframe, how_many_bars=how_many_bars, export_dir="csv_export")

            # load_data.export_to_csv_from_df(ticket=ticket, timeframe=timeframe, data=data, export_dir=os.path.join(current_dir, "csv_export"))
            #
            # #load_data.always_get_share_data(ticket="EURUSD", timeframe=mt5.TIMEFRAME_M1)
            # #load_data.always_get_share_data(ticket="EURUSD", timeframe=mt5.TIMEFRAME_M5)
            # #load_data.always_get_share_data(ticket="EURUSD", timeframe=mt5.TIMEFRAME_M15)
            # #load_data.always_get_share_data(ticket="EURUSD", timeframe=mt5.TIMEFRAME_M30)
            # #load_data.always_get_share_data(ticket="EURUSD", timeframe=mt5.TIMEFRAME_H1)
            # #load_data.always_get_share_data(ticket="EURUSD", timeframe=mt5.TIMEFRAME_H4)
            # load_data.always_get_share_data(ticket="EURUSD", timeframe=mt5.TIMEFRAME_D1)
            #
            # load_data.disconnect_from_metatrader5()

checking_currency()


# @shared_task(name="checking_currency")
# def checking_currency():
#     load_data = SharesDataLoader('EURUSDrfd')
#     load_data.connect_to_metatrader5(path=f"C:\Program Files\MetaTrader 5 Alfa-Forex\terminal64.exe")
#     load_data.connect_to_db(host=env("DB_HOST"),
#                             user=env("DB_USER"),
#                             password=env("DB_PASSWORD"),
#                             dbname=env("DB_NAME"))
#
#     load_data.always_get_share_data(ticket="EURUSDrfd", timeframe=mt5.TIMEFRAME_H1)

# load_data.disconnect_from_metatrader5()

# checking_currency()

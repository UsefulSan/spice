import asyncio
from datetime import datetime, timedelta

import pandas as pd
from celery import shared_task

from core.scripts.get_currency_data import SharesDataLoader
from core.scripts.main_value_currency import currency
from spice.settings import env

pd.set_option('display.max_columns', 10)  # сколько столбцов показываем
pd.set_option('display.width', 1500)  # макс. ширина таблицы для показа

load_data = SharesDataLoader('poher')
load_data.connect_to_metatrader5(path='C:\Program Files\MetaTrader 5 Alfa-Forex\terminal64.exe')


@shared_task(name="checking_currency")
async def checking_currency():
    how_many_bars = 1

    utc_till = datetime.now() + timedelta(days=1)  # получим данные по завтрашний день
    # utc_till = datetime.now() - timedelta(days=1)  # получим данные по вчерашний день
    strategy_tasks = []
    for timeframe_name, timeframe in currency.timeframe.items():
        for ticket in currency.tickers:
            load_data = SharesDataLoader(ticket)
            # load_data.connect_to_metatrader5(path='C:\Program Files\MetaTrader 5 Alfa-Forex\terminal64.exe')
            load_data.connect_to_db(
                host=env("DB_HOST"),
                user=env("DB_USER"),
                password=env("DB_PASSWORD"),
                dbname=env("DB_NAME"))
            # data = load_data.get_share_data(ticket=ticket, timeframe=timeframe[0], utc_till=utc_till,
            #                                 how_many_bars=how_many_bars)
            # print(f'Currency name: {ticket.replace("rfd", "")}-{timeframe_name}\n', data)

            strategy_tasks.append(asyncio.create_task(load_data.always_get_share_data(
                ticket=ticket, timeframe_name=timeframe_name, timeframe=timeframe)))

            # load_data.disconnect_from_metatrader5()
    await asyncio.gather(*strategy_tasks)


#     yield print(ticket)
# async def check(ticket):
#     async for ch in checking_currency(ticket):
#         print(ch)
#
start = datetime.now()

loop = asyncio.get_event_loop()
task = loop.create_task(checking_currency())
loop.run_until_complete(task)
# try:
#     loop.run_until_complete(asyncio.gather(check('EURUSDrfd'), check('GBPUSDrfd'), check('USDJPYrfd'), check('USDCADrfd')))
# finally:
#     loop.close()

# asyncio.run(checking_currency())
# checking_currency()
end = datetime.now() - start
print(end)

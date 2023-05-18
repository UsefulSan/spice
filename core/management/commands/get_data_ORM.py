from datetime import datetime

from django.core.management.base import BaseCommand
from core.scripts.get_currency_data import SharesDataLoader
from core.scripts.main_value_currency import currency
from datetime import datetime, timedelta

how_many_bars = 1
utc_till = datetime.now() + timedelta(days=1)

class Command(BaseCommand):
    help = "Загружает исторические датафреймы валюты с MT5 с помощью ORM"

    def handle(self, *args, **options):
        for timeframe_name, timeframe in currency.timeframe.items():
            for ticket in currency.tickers:
                loader = SharesDataLoader(ticket)
                loader.connect_to_metatrader5(path='C:\Program Files\MetaTrader 5 Alfa-Forex\terminal64.exe')
                loader.get_share_data(ticket=ticket, timeframe=timeframe[0], utc_till=utc_till,
                                            how_many_bars=how_many_bars)
                print(f'Currency name: {ticket.replace("rfd", "")}-{timeframe_name}\n', data)

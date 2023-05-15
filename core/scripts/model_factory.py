from core.scripts.main_value_currency import currency
from spice.settings import BASE_DIR


def create_new_models():
    for timeframe in currency.timeframe.keys():
        for ticket in currency.tickers:
            with open(f'{BASE_DIR}\core\models\{ticket.lower().replace("rfd", "")}_'
                      f'{timeframe.lower()}.py', 'w+') as f:
                f.write(f'from core.models import CurrencyMixin\n'
                        f'class {ticket.replace("rfd", "")}_{timeframe}(CurrencyMixin):\n'
                        f'  pass')
    print('Модели созданы')


create_new_models()

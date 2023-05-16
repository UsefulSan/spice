from core.scripts.main_value_currency import currency
from spice.settings import BASE_DIR


def create_new_models() -> None:
    """
    Создает модели в файле factory_models.py, на основе таймфремов и тикеров из class ValueCurrency
    """
    with open(f'{BASE_DIR}\core\models\\factory_models.py', 'w+') as f:
        f.write(f'from core.models import CurrencyMixin\n')
        for timeframe in currency.timeframe.keys():
            for ticket in currency.tickers:
                f.write(f'class {ticket.replace("rfd", "")}_{timeframe}(CurrencyMixin):\n'
                        f'  pass\n\n')

    print('Модели созданы')


create_new_models()

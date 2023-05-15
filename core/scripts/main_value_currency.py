import mt5


class ValueCurrency:
    def __init__(self):
        """
        tickers
        """
        self.tickers = {
            'EURUSDrfd',
            'GBPUSDrfd',
            'USDJPYrfd',
            'USDCADrfd',
        }

        """
        timeframes
        """
        self.timeframe = {
            # "MN1": (mt5.TIMEFRAME_MN1,), # если не будет второго значения, то упадет в ошибку
            "W1": (mt5.TIMEFRAME_W1, 60480000),
            "D1": (mt5.TIMEFRAME_D1, 8640000),
            "H4": (mt5.TIMEFRAME_H4, 14400),
            "H1": (mt5.TIMEFRAME_H1, 3600),
            "M30": (mt5.TIMEFRAME_M30, 1800),
            "M15": (mt5.TIMEFRAME_M15, 900),
            "M5": (mt5.TIMEFRAME_M5, 300),
            "M1": (mt5.TIMEFRAME_M1, 60)
        }


currency = ValueCurrency()


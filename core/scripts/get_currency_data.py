from datetime import datetime, timedelta

import MetaTrader5 as mt5  # импортируем модуль для подключения к MetaTrader5
import cv2
import pandas as pd  # импортируем модуль pandas для вывода полученных данных в табличной форме
import psycopg2  # импортируем модуль для работы с БД postgresql
import pytz  # импортируем модуль pytz для работы с таймзоной
from pandas import DataFrame


class SharesDataLoader():
    """Класс для загрузки данных с MetaTrader5"""

    def __init__(self, share_name):
        self.share_name = share_name
        self.conn = None
        self.cursor = None
        self.connection_to_db = False
        self.how_many_bars_max = 1000

        self.timezone = pytz.timezone("Etc/UTC")  # установим таймзону в UTC
        self.local_timezone = pytz.timezone("Europe/Moscow")

        # создадим объект datetime в таймзоне UTC, чтобы не применялось смещение локальной таймзоны
        # self._utc_till = datetime.datetime.now(self.timezone)# datetime.datetime(2021, 10, 10, tzinfo=self.timezone)

    def connect_to_metatrader5(self, path: str) -> None:
        """
        Подключение к установленному приложению Metatrader5.
        """
        mt5.initialize(path=path)
        # установим подключение к терминалу MetaTrader 5
        if not mt5.initialize():
            print("connection to MetaTrader5 failed, error code =", mt5.last_error())
            # завершим подключение к терминалу MetaTrader 5
            mt5.shutdown()
            quit()
        else:
            print("Connection to MetaTrader5: OK")

    def disconnect_from_metatrader5(self) -> None:
        """
        Отключение от Metatrader5
        """
        if self.connection_to_db:
            self.conn.close()
            print("Disconnection from db: OK")
        mt5.shutdown()
        print("Disconnection from MetaTrader5: OK")

    def connect_to_db(self, host: str, user: str, password: str, dbname: str) -> None:
        """
        Подключение к PostgreSQL ДБ
        """
        try:
            self.conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)
            self.cursor = self.conn.cursor()
            self.connection_to_db = True
            print("Connection to db: OK")
        except psycopg2.Error as ex:
            print("connection to DB failed, error code =", ex)
            quit()

    def get_share_data(self, ticket: str, timeframe: int, utc_till: datetime, how_many_bars: int) -> DataFrame:
        rates = mt5.copy_rates_from(ticket, timeframe, utc_till, how_many_bars)
        # создадим из полученных данных DataFrame
        rates_frame: DataFrame = pd.DataFrame(rates)
        # сконвертируем время в виде секунд в формат datetime
        if len(rates_frame.index):
            rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        return rates_frame

    def get_share_data_from_db(self, ticket: str, timeframe_name : str, how_many_bars: int) -> DataFrame:

        table_name = ticket + "_" + timeframe_name
        self.cursor.execute(
            "SELECT time, open, high, low, close, volume FROM `" + table_name + "`" + " ORDER BY time DESC LIMIT " +
            str(how_many_bars)
        )

        # Get all data from table
        rows = self.cursor.fetchall()
        dataframe = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", "Close", "Volume"])
        dataframe = dataframe[::-1].reset_index(drop=True)  # Reverse Ordering of DataFrame Rows + Reset index
        # print(dataframe.dtypes)
        return dataframe

    def always_get_share_data(self, ticket: str, timeframe_name : str, timeframe: dict[int]) -> None:
        """
        Сначала обновляет исторические данные о валюте в БД, потом ожидает появления нового фрейма, забирает его и
        добаляет в БД
        @param timeframe_name : Сокращенное название валюты
        @param ticket: Название валюты на бирже
        @param timeframe: Временной отрезок в секундах
        """
        _timeframe = "D1"
        how_many_bars = 0

        table_name = ("core_" + ticket.replace('rfd', '') + "_" + timeframe_name).lower()

        # ----------------------- UPDATE HISTORY -----------------------
        while True:
            # let's execute our query to db
            self.cursor.execute(
                "SELECT max(time) FROM " + table_name
            )

            # Get all data from table
            rows = self.cursor.fetchall()
            last_bar_time = 0

            if rows[0][0] == None:
                how_many_bars = self.how_many_bars_max
            else:
                last_bar_time = rows[0][0]
                # print(last_bar_time)

                # calc missed bars
                today = datetime.now(tz=self.timezone)  # Проверить верность времени
                # today_utc = datetime.datetime(today.year, today.month, today.day, today.hour, today.minute,
                #                               today.second, tzinfo=self.timezone)
                # print(today)
                # print(last_bar_time)
                how_many_bars = int(((today - last_bar_time).total_seconds()) // timeframe[1] + 1)
                # print(today, last_bar_time)
                # print((today - last_bar_time))
                # print((today - last_bar_time).total_seconds())
                # print(timeframe[1])
                print(f'Quantity bars to load: {how_many_bars}\n')


            # # получим данные по завтрашний день
            utc_till = datetime.now(tz=self.timezone) + timedelta(days=1)
            # print(utc_till)
            # a = datetime.datetime.now(tz=self.timezone) - datetime.timedelta(hours=3)
            a = datetime.utcnow() - datetime.now()
            # print(f'{a} ЗДЕСЬЬЬ')
            rates = mt5.copy_rates_from(ticket, timeframe[0], utc_till, how_many_bars)
            # print(rates)
            # создадим из полученных данных DataFrame
            rates_frame = pd.DataFrame(rates)
            # print(rates_frame)
            # Подсчет отклонения временных зон в часах
            if datetime.utcnow() < datetime.now():
                time_zone_difference = int((datetime.now() - datetime.utcnow()).seconds / 3600)
            else:
                time_zone_difference = -int((datetime.utcnow() - datetime.now()).seconds / 3600)
            # сконвертируем время в виде секунд в формат datetime
            if len(rates_frame):
                rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s', utc=True)  # Проверить время utc
                rates_frame['time'] = rates_frame['time'] - timedelta(hours=time_zone_difference)
            # print(type(rates_frame))
            # print(rates_frame)

            # выведем данные
            # print("\nВыведем датафрейм с данными")
            # print(rates_frame)

            for i in range(len(rates_frame)):  # последний бар не берем -1 т.к. он еще формируется.
                # for i in range(len(rates_frame.index) - 1): #  !!! Возможно здесь надо будет -1
                _time = rates_frame.at[i, "time"]
                _open = rates_frame.at[i, "open"]
                _high = rates_frame.at[i, "high"]
                _low = rates_frame.at[i, "low"]
                _close = rates_frame.at[i, "close"]
                _tick_volume = rates_frame.at[i, "tick_volume"]
                _real_volume = rates_frame.at[i, "real_volume"]
                # print(i, _time, _open, _high, _low, _close, _tick_volume, _real_volume)

                if ((rows[0][0] != None) and (_time > last_bar_time)) or ((rows[0][0] == None)):
                    # let's insert row in table
                    self.cursor.execute(
                        "INSERT INTO " + table_name + " (time, open, high, low, close, real_volume, tick_volume) "
                                                      "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (_time, _open, _high, _low, _close, int(_real_volume), int(_tick_volume)))

            # to commit changes to db!!!
            # run this command:
            self.conn.commit()

            last_bar_time = rates_frame.at[len(rates_frame.index) - 1, "time"]
            # print(last_bar_time)

            next_bar_time = last_bar_time + timedelta(seconds=timeframe[1])
            # print(next_bar_time)

            if next_bar_time > datetime.now(tz=self.timezone):  # Проверить время utc
                break

        # ----------------------- Update in Real Time -----------------------
        # while True:
        #     next_bar_time = last_bar_time + datetime.timedelta(seconds=timeframe[1])
        #     wait_for_calculated = int(
        #         (next_bar_time - datetime.datetime.now(tz=self.timezone)).total_seconds())  # Проверить время utc
        #     print("Last bar time: %s Next bar time: %s" % (last_bar_time, next_bar_time))
        #     print('=' * 75)
        #     # print("waiting %s seconds..." % (wait_for_calculated))
        #
        #     # cv2.waitKey(abs(wait_for_calculated*1000+500)) # 500 milsec delay
        #     for sec in range(abs(wait_for_calculated)):
        #         if ((sec + 1) % 30 == 0):
        #             print(wait_for_calculated - sec)
        #         else:
        #             print(wait_for_calculated - sec, end=" ")
        #         cv2.waitKey(1000)
        #
        #     # add new data to table
        #     # print(datetime.datetime.now())
        #     print("Last bar time: %s Next bar time: %s" % (last_bar_time, next_bar_time))
        #     # check_last_bar_writed_to_db = get_last_bar_time(cursor)
        #     # print(check_last_bar_writed_to_db)
        #     # if (last_bar_time == check_last_bar_writed_to_db):
        #     #     print("Ok")
        #     # else:
        #     #     print("Failed write to DB!")
        #     # ...
        #
        #     # calc missed bars
        #     today = datetime.datetime.now(tz=self.timezone)  # Проверить время utc
        #     num_bars_to_load = ((
        #                                 today - last_bar_time).total_seconds()) // timeframe[
        #                            1] + 5  # берем +5 бар назад
        #     print(num_bars_to_load)
        #
        #     how_many_bars = int(num_bars_to_load)
        #
        #     # получим данные по завтрашний день
        #     utc_till = datetime.datetime.now() + datetime.timedelta(days=1)
        #     print(utc_till)
        #
        #     # exit(1)
        #
        #     check_we_have_next_bar_loaded = False
        #     while not check_we_have_next_bar_loaded:
        #         rates = mt5.copy_rates_from(ticket, timeframe, utc_till, how_many_bars)
        #
        #         # создадим из полученных данных DataFrame
        #         rates_frame = pd.DataFrame(rates)
        #         # сконвертируем время в виде секунд в формат datetime
        #         if len(rates_frame.index):
        #             rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        #
        #         # проверка, что есть данные следующей свечи
        #         for i in range(len(rates_frame.index)):
        #             _time = rates_frame.at[i, "time"]
        #             if _time > last_bar_time:
        #                 check_we_have_next_bar_loaded = True
        #                 print("We have got next bar from Metatrader")
        #             else:
        #                 print("Will try again - to get next bar ... ")
        #                 cv2.waitKey(500)  # 500 milsec delay
        #
        #     # выведем данные
        #     print("\nВыведем датафрейм с данными")
        #     print(rates_frame)
        #
        #     for i in range(len(rates_frame.index)):
        #         _time = rates_frame.at[i, "time"]
        #         _open = rates_frame.at[i, "open"]
        #         _high = rates_frame.at[i, "high"]
        #         _low = rates_frame.at[i, "low"]
        #         _close = rates_frame.at[i, "close"]
        #         _tick_volume = rates_frame.at[i, "tick_volume"]
        #         _real_volume = rates_frame.at[i, "real_volume"]
        #         print(i, _time, _open, _high, _low, _close, _tick_volume, _real_volume)
        #
        #         if _time >= last_bar_time and _time < next_bar_time:
        #             # let's insert row in table
        #             self.cursor.execute(
        #                 "INSERT INTO " + table_name + " (time, open, high, low, close, real_volume, tick_volume) "
        #                                               "VALUES (%s, %s, %s, %s, %s, %s, %s)",
        #                 (_time, _open, _high, _low, _close, int(_real_volume), int(_tick_volume)))
        #
        #     # to commit changes to db!!!
        #     # run this command:
        #     self.conn.commit()
        #
        #     last_bar_time = next_bar_time
        # # ----------------------- Update in Real Time -----------------------

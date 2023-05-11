import datetime
import os

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
        self.how_many_bars_max = 50000

        self.timezone = pytz.timezone("Etc/UTC")  # установим таймзону в UTC
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

    def get_share_data_from_db(self, ticket: str, timeframe: int, how_many_bars: int) -> DataFrame:
        if timeframe == mt5.TIMEFRAME_D1:   timeframe = "D1"
        if timeframe == mt5.TIMEFRAME_H4:   timeframe = "H4"
        if timeframe == mt5.TIMEFRAME_H1:   timeframe = "H1"
        if timeframe == mt5.TIMEFRAME_M30:  timeframe = "M30"
        if timeframe == mt5.TIMEFRAME_M15:  timeframe = "M15"
        if timeframe == mt5.TIMEFRAME_M5:   timeframe = "M5"
        if timeframe == mt5.TIMEFRAME_M1:   timeframe = "M1"

        table_name = ticket + "_" + timeframe
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

    def export_to_csv_from_df(self, ticket, timeframe, data, export_dir):
        _timeframe = "D1"
        if timeframe == mt5.TIMEFRAME_MN1:   _timeframe = "MN1"
        if timeframe == mt5.TIMEFRAME_W1:   _timeframe = "W1"
        if timeframe == mt5.TIMEFRAME_D1:   _timeframe = "D1"
        if timeframe == mt5.TIMEFRAME_H4:   _timeframe = "H4"
        if timeframe == mt5.TIMEFRAME_H1:   _timeframe = "H1"
        if timeframe == mt5.TIMEFRAME_M30:  _timeframe = "M30"
        if timeframe == mt5.TIMEFRAME_M15:  _timeframe = "M15"
        if timeframe == mt5.TIMEFRAME_M5:   _timeframe = "M5"
        if timeframe == mt5.TIMEFRAME_M1:   _timeframe = "M1"

        print(ticket)
        print(data)
        data = data[["time", "open", "high", "low", "close", "real_volume"]]
        data.rename(columns={"time": "datetime", "real_volume": "volume"}, inplace=True)

        if not os.path.exists(export_dir): os.makedirs(export_dir)
        data.to_csv(os.path.join(export_dir, ticket + "_" + _timeframe + ".csv"), index=False, encoding='utf-8')

    def export_to_csv(self, ticket, timeframe, how_many_bars, export_dir):
        _timeframe = "D1"
        if timeframe == mt5.TIMEFRAME_MN1:  _timeframe = "MN1"
        if timeframe == mt5.TIMEFRAME_W1:   _timeframe = "W1"
        if timeframe == mt5.TIMEFRAME_D1:   _timeframe = "D1"
        if timeframe == mt5.TIMEFRAME_H4:   _timeframe = "H4"
        if timeframe == mt5.TIMEFRAME_H1:   _timeframe = "H1"
        if timeframe == mt5.TIMEFRAME_M30:  _timeframe = "M30"
        if timeframe == mt5.TIMEFRAME_M15:  _timeframe = "M15"
        if timeframe == mt5.TIMEFRAME_M5:   _timeframe = "M5"
        if timeframe == mt5.TIMEFRAME_M1:   _timeframe = "M1"

        table_name = ticket + "_" + _timeframe
        self.cursor.execute(
            "SELECT time, open, high, low, close, volume FROM `" + table_name + "`" + " ORDER BY time DESC LIMIT " + str(
                how_many_bars)
        )

        # Get all data from table
        rows = self.cursor.fetchall()
        dataframe = pd.DataFrame(rows, columns=["Date", "Open", "High", "Low", "Close", "Volume"])
        dataframe = dataframe[::-1].reset_index(drop=True)  # Reverse Ordering of DataFrame Rows + Reset index

        if not os.path.exists(export_dir): os.makedirs(export_dir)
        dataframe.to_csv(os.path.join(export_dir, ticket + "_" + _timeframe + ".csv"), index=False, encoding='utf-8')

    def always_get_share_data(self, ticket: str, timeframe: int) -> None:
        """
        Сначала обновляет исторические данные о валюте в БД, потом ожидает появления нового фрейма, забирает его и
        добаляет в БД
        @param ticket: Название валюты на бирже
        @param timeframe: Временной отрезок
        """
        _timeframe = "D1"
        how_many_bars = 0
        time_in_seconds_bar = 0
        if timeframe == mt5.TIMEFRAME_D1:   time_in_seconds_bar = 86400  # 60*60*24
        if timeframe == mt5.TIMEFRAME_H4:   time_in_seconds_bar = 14400  # 60*60*4
        if timeframe == mt5.TIMEFRAME_H1:   time_in_seconds_bar = 3600  # 60*60
        if timeframe == mt5.TIMEFRAME_M30:  time_in_seconds_bar = 1800  # 60*30
        if timeframe == mt5.TIMEFRAME_M15:  time_in_seconds_bar = 900  # 60*15
        if timeframe == mt5.TIMEFRAME_M5:   time_in_seconds_bar = 300  # 60*5
        if timeframe == mt5.TIMEFRAME_M1:   time_in_seconds_bar = 60  # 60

        if timeframe == mt5.TIMEFRAME_MN1:  _timeframe = "MN1"
        if timeframe == mt5.TIMEFRAME_W1:   _timeframe = "W1"
        if timeframe == mt5.TIMEFRAME_D1:   _timeframe = "D1"
        if timeframe == mt5.TIMEFRAME_H4:   _timeframe = "H4"
        if timeframe == mt5.TIMEFRAME_H1:   _timeframe = "H1"
        if timeframe == mt5.TIMEFRAME_M30:  _timeframe = "M30"
        if timeframe == mt5.TIMEFRAME_M15:  _timeframe = "M15"
        if timeframe == mt5.TIMEFRAME_M5:   _timeframe = "M5"
        if timeframe == mt5.TIMEFRAME_M1:   _timeframe = "M1"

        table_name = ("core_" + ticket.replace('rfd', '') + "_" + _timeframe).lower()

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
                print(last_bar_time)

                # calc missed bars
                today = datetime.datetime.now(tz=self.timezone)  # Проверить верность времени
                # today_utc = datetime.datetime(today.year, today.month, today.day, today.hour, today.minute,
                #                               today.second, tzinfo=self.timezone)
                print(today)
                print(last_bar_time)
                num_bars_to_load = ((today - last_bar_time).total_seconds()) // time_in_seconds_bar + 1
                print(num_bars_to_load)

                how_many_bars = int(num_bars_to_load)

            # получим данные по завтрашний день
            utc_till = datetime.datetime.now() + datetime.timedelta(days=1)
            print(utc_till)
            rates = mt5.copy_rates_from(ticket, timeframe, utc_till, how_many_bars)

            # создадим из полученных данных DataFrame
            rates_frame = pd.DataFrame(rates)
            # сконвертируем время в виде секунд в формат datetime
            if len(rates_frame.index):
                rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s', utc=True)  # Проверить время utc

            # выведем данные
            print("\nВыведем датафрейм с данными")
            print(rates_frame)

            for i in range(len(rates_frame.index) - 1):  # последний бар не берем -1 т.к. он еще формируется
                _time = rates_frame.at[i, "time"]
                _open = rates_frame.at[i, "open"]
                _high = rates_frame.at[i, "high"]
                _low = rates_frame.at[i, "low"]
                _close = rates_frame.at[i, "close"]
                _tick_volume = rates_frame.at[i, "tick_volume"]
                _real_volume = rates_frame.at[i, "real_volume"]
                print(i, _time, _open, _high, _low, _close, _tick_volume, _real_volume)

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
            print(last_bar_time)

            next_bar_time = last_bar_time + datetime.timedelta(seconds=time_in_seconds_bar)
            print(next_bar_time)

            if next_bar_time > datetime.datetime.now(tz=self.timezone):  # Проверить время utc
                break

        # ----------------------- Update in Real Time -----------------------
        while True:
            next_bar_time = last_bar_time + datetime.timedelta(seconds=time_in_seconds_bar)
            wait_for_calculated = int(
                (next_bar_time - datetime.datetime.now(tz=self.timezone)).total_seconds())  # Проверить время utc
            print("Last bar time: %s Next bar time: %s" % (last_bar_time, next_bar_time))
            print("waiting %s seconds..." % (wait_for_calculated))

            # cv2.waitKey(abs(wait_for_calculated*1000+500)) # 500 milsec delay
            for sec in range(abs(wait_for_calculated)):
                if ((sec + 1) % 30 == 0):
                    print(wait_for_calculated - sec)
                else:
                    print(wait_for_calculated - sec, end=" ")
                cv2.waitKey(1000)

            # add new data to table
            # print(datetime.datetime.now())
            print("Last bar time: %s Next bar time: %s" % (last_bar_time, next_bar_time))
            # check_last_bar_writed_to_db = get_last_bar_time(cursor)
            # print(check_last_bar_writed_to_db)
            # if (last_bar_time == check_last_bar_writed_to_db):
            #     print("Ok")
            # else:
            #     print("Failed write to DB!")
            # ...

            # calc missed bars
            today = datetime.datetime.now(tz=self.timezone)  # Проверить время utc
            num_bars_to_load = ((
                                            today - last_bar_time).total_seconds()) // time_in_seconds_bar + 5  # берем +5 бар назад
            print(num_bars_to_load)

            how_many_bars = int(num_bars_to_load)

            # получим данные по завтрашний день
            utc_till = datetime.datetime.now() + datetime.timedelta(days=1)
            print(utc_till)

            # exit(1)

            check_we_have_next_bar_loaded = False
            while not check_we_have_next_bar_loaded:
                rates = mt5.copy_rates_from(ticket, timeframe, utc_till, how_many_bars)

                # создадим из полученных данных DataFrame
                rates_frame = pd.DataFrame(rates)
                # сконвертируем время в виде секунд в формат datetime
                if len(rates_frame.index):
                    rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

                # проверка, что есть данные следующей свечи
                for i in range(len(rates_frame.index)):
                    _time = rates_frame.at[i, "time"]
                    if _time > last_bar_time:
                        check_we_have_next_bar_loaded = True
                        print("We have got next bar from Metatrader")
                    else:
                        print("Will try again - to get next bar ... ")
                        cv2.waitKey(500)  # 500 milsec delay

            # выведем данные
            print("\nВыведем датафрейм с данными")
            print(rates_frame)

            for i in range(len(rates_frame.index)):
                _time = rates_frame.at[i, "time"]
                _open = rates_frame.at[i, "open"]
                _high = rates_frame.at[i, "high"]
                _low = rates_frame.at[i, "low"]
                _close = rates_frame.at[i, "close"]
                _tick_volume = rates_frame.at[i, "tick_volume"]
                _real_volume = rates_frame.at[i, "real_volume"]
                print(i, _time, _open, _high, _low, _close, _tick_volume, _real_volume)

                if _time >= last_bar_time and _time < next_bar_time:
                    # let's insert row in table
                    self.cursor.execute(
                        "INSERT INTO " + table_name + " (time, open, high, low, close, real_volume, tick_volume) "
                                                      "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (_time, _open, _high, _low, _close, int(_real_volume), int(_tick_volume)))

            # to commit changes to db!!!
            # run this command:
            self.conn.commit()

            last_bar_time = next_bar_time
        # # ----------------------- Update in Real Time -----------------------

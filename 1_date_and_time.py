"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta, date
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU')


def print_days():
    delta = timedelta(days=1)
    today = date.today()
    format = '%d %B %Y - %A'

    print("Вчера: ", (today - delta).strftime(format))
    print("Сегодня: ", today.strftime(format))
    print("30 дней назад: ", (today - 30 * delta).strftime(format))


def str_2_datetime(date_string):
    dfs = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return dfs

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

import datetime
from datetime import date


def count_days(date: datetime.date, month: int) -> int:
    c = 1
    if date.month == 1:
        c += 31 - date.day
    elif date.month == 2:
        if (date.year % 4 == 0 and date.year % 100 != 0) or date.year % 400 == 0:
            c += 29 - date.day
        else:
            c += 28 - date.day
    elif date.month in (4, 6, 9, 11):
        c += 30 - date.day
    else:
        c += 31 - date.day
    for m in range(date.month + 1, month):
        if m in (4, 6, 9, 11):
            c += 30
        elif m == 2:
            if (date.year % 4 == 0 and date.year % 100 != 0) or date.year % 400 == 0:
                c += 29
            else:
                c += 28
        else:
            c += 31
    return c


try:
    user_date = date(*[int(i) for i in input('Введите дату в формате дд.мм.гггг: ').split('.')][::-1])
    current_day = date.today()
    if (current_day - user_date).days < 0:
        raise ValueError
except ValueError:
    print('Упс! Некорректные данные!')
print((current_day - user_date).days)

res = 0
if current_day != user_date:
    if current_day.month > user_date.month:
        res += count_days(user_date, current_day.month)
        res += current_day.day - user_date.day
        y = user_date.year
    elif current_day.month < user_date.month or (
            current_day.month == user_date.month and current_day.day < user_date.day):
        res += count_days(user_date, 13)
        res += count_days(date(user_date.year + 1, 1, 1), current_day.month)
        res += current_day.day - 1
        y = user_date.year + 1
    else:
        res += current_day.day - user_date.day
        y = user_date.year

    if current_day.year != user_date.year:
        while y != current_day.year:
            if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
                res += 366
            else:
                res += 365
            y += 1

print(res)

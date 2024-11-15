import datetime

days, seconds = int(input()), int(input())


def shift_time(days: int, seconds: int):
    data_time_ = datetime.datetime(2023,1,1,12,30)
    data_shift = datetime.timedelta(days = days, seconds = seconds)
    return tuple(map(int, str.split((data_time_ + data_shift).strftime("%d %S"))))


print(shift_time(days, seconds))

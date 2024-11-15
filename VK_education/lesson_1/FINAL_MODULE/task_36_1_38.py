import datetime

string_datetime = input()


def parse_time(s):
    parse_str = s.split()
    date_ =  datetime.datetime(int(parse_str[0]), int(parse_str[1]), int(parse_str[2]), int(parse_str[3]), int(parse_str[4]), int(parse_str[5]))
    delta_days = datetime.timedelta(days = 1)
    return int(str((date_ + delta_days).strftime("%d")))

print(parse_time(string_datetime))
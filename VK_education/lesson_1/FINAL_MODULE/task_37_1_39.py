import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    count_l = []
    for date in dates:
        d_t = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        count_l.append(int(datetime.datetime.strftime(d_t, "%m")))
    counter_c = Counter(count_l)
    return [month for month, x in counter_c.most_common(n)]



# if __name__ == '__main__':
#     dates = ["2023-01-01T23:59:59", "2023-01-01T23:59:59", "2023-02-01T23:59:59"]
#     print(most_common_months(dates, 2))
#
#     dates = ["2023-01-01T23:59:59", "2023-01-01T23:59:59", "2023-02-01T23:59:59", "2023-03-01T23:59:59",
#              "2023-02-02T23:59:59", "2023-02-01T23:59:59", "2023-05-01T23:59:59", "2023-01-01T23:59:59"]
#     print(most_common_months(dates, 3))

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
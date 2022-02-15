from datetime import datetime
import calendar
import pandas as pd

# , index_col=['num1', 'num2', 'num3', 'date1', 'date2', 'date3']
df = pd.read_csv('tasks.csv', header=None, skiprows=2)

# 1 Сколько четных чисел в этом столбце?
vals = df[1].values
num1_ans = len([x for x in vals if x % 2 == 0])

# 2 Сколько простых чисел в этом столбце?
vals = df[2].values


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if not num % i:
            return False
    return True


num2_ans = len([x for x in vals if is_prime(x)])


# 3 Сколько чисел, меньших 0.5 в этом столбце?
vals = df[3].values
for i in range(len(vals)):
    vals[i].replace(',', '.')
    vals[i] = ''.join([x for x in vals[i] if x in '.0123456789'])
num3_ans = len([x for x in vals if float(x) < 0.5])

# 4 Столько вторников в этом столбце?
vals = df[4].values
# # Mon Aug  6 07:11:19 2018
# for date in vals:
#     datetime_object = datetime.strptime(date, '%A %B  %d %H:%M:%S %Y')
num4_ans = len([x for x in vals if 'Thu' in x])


# 5 Сколько вторников в этом столбце?
# 2026-07-19 08:15:41.695463
vals = df[5].values
for i in range(len(vals)):
    vals[i] = datetime.strptime(vals[i], '%Y-%m-%d %H:%M:%S.%f')
    vals[i] = vals[i].weekday()
num5_ans = len([x for x in vals if x == 1])


# Сколько последних вторников месяца в этом столбце?
vals = df[6].values
# 10-04-2011
num6_ans = 0
for i in range(len(vals)):
    vals[i] = datetime.strptime(vals[i], '%m-%d-%Y')
    month_len = calendar.monthrange(vals[i].year, vals[i].month)[1]
    if month_len - vals[i].day < 7:
        num6_ans += 1




if __name__ == "__main__":
    print(num1_ans)
    print(num2_ans)
    print(num3_ans)
    print(num4_ans)
    print(num5_ans)
    print(num6_ans)


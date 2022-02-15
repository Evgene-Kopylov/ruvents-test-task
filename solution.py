from datetime import datetime
import calendar

import pandas as pd

df = pd.read_csv('tasks.csv', header=None, skiprows=2)

# 1 Сколько четных чисел в этом столбце?
vals = df[1].values


def task_1(vals):
    return len([x for x in vals if x % 2 == 0])


num1_ans = task_1(vals)

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


def task_3(vals):
    for i in range(len(vals)):
        vals[i] = vals[i].replace(',', '.')
        vals[i] = ''.join([j for j in vals[i] if j in '.0123456789'])
    return len([x for x in vals if float(x) < 0.5])


num3_ans = task_3(vals)

# 4 Столько вторников в этом столбце?
vals = df[4].values
num4_ans = len([x for x in vals if 'Thu' in x])

# 5 Сколько вторников в этом столбце?
# 2026-07-19 08:15:41.695463
vals = df[5].values


def task_5(vals):
    for i in range(len(vals)):
        vals[i] = datetime.strptime(vals[i], '%Y-%m-%d %H:%M:%S.%f')
        vals[i] = vals[i].weekday()
    return len([x for x in vals if x == 1])


num5_ans = task_5(vals)

# Сколько последних вторников месяца в этом столбце?
vals = df[6].values


# 10-04-2011

def task_6(vals):
    num6_ans = 0
    for i in range(len(vals)):
        vals[i] = datetime.strptime(vals[i], '%m-%d-%Y')
        month_len = calendar.monthrange(vals[i].year, vals[i].month)[1]
        if month_len - vals[i].day < 7:
            num6_ans += 1
    return num6_ans


num6_ans = task_6(vals)

if __name__ == "__main__":
    print(num1_ans)
    print(num2_ans)
    print(num3_ans)
    print(num4_ans)
    print(num5_ans)
    print(num6_ans)

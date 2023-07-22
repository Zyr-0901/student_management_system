import calendar


def for_shediao():
    result = []
    for i in range(1, 101):
        if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
            result.append(i)
    return result


def while_shediao():
    i = 1
    b = []
    while i < 101:
        if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
            b.append(i)
        i += 1
    return b


def demo_3():
    chicken_num = (35 * 4 - 94) / 2
    rabbit_num = 35 - chicken_num
    print(f"鸡有 {int(chicken_num)}只")
    print(f"兔子有{int(rabbit_num)}只")


def demo_4():
    # 设鸡有x只
    for x in range(1, 36):
        if x * 2 + (35 - x) * 4 == 94:
            print(f"鸡有{x}只")
            print(f"兔子有{35 - x}只")

#
def demo_5(year):
    # 判断一年有多少天
    # 判断第一天是周几
    # 判断剩下的周期
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days = 365
    # 判断是否为闰年
    if calendar.isleap(year):
        days = 366
    begin = calendar.weekday(year, 1, 1)
    residue_days = days%7
    if residue_days == 1:
        print(weekdays[begin])
    if residue_days == 2:
        if begin == 6:
            print(weekdays[begin], weekdays[0])
        else:
            print(weekdays[begin], weekdays[begin+1])


if __name__ == '__main__':
    # print(for_shediao())
    # print(while_shediao())
    # demo_3()
    # demo_4()
    # demo_5(2022)
    # demo_5(2020)
    demo_5(1984)

def valid_demo():
    column1 = ["张三", 123, "", "@#!$%"]
    column2 = [45, 1, 99, 2, 98, 0, 100, -12, 3.4, "测试血量"]
    column3 = [40, 0, -2, "测试攻击力"]

    for item1 in column1:
        for item2 in column2:
            for item3 in column3:
                print(f" - [{item1}, {item2}, {item3}]")


def invalid_demo():
    column1 = ["张三", 123, "", "@#!$%"]
    column2 = [0, 100, -12, 3.4, "测试血量"]
    column3 = [-2, "测试攻击力"]

    for item1 in column1:
        for item2 in column2:
            for item3 in column3:
                print(f" - [{item1}, {item2}, {item3}]")


if __name__ == '__main__':
    # demo()
    valid_demo()

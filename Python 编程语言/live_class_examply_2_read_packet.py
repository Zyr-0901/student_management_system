# 抢红包
# 群主发红包
# 成员抢红包
# 抢到红包报数
import random


class Person:
    def __init__(self, name: str, money: int):
        self.name = name
        self.money = money

    def show(self):
        return f"{self.name},当前金额{self.money}"


class Manage(Person):
    def send(self, money, num):
        if money > self.money:
            print("余额不足")
        else:
            result = []
            value = money // num
            remainder = money % num
            for i in range(1, num):
                result.append(value)
            result.append(remainder)
            self.money -= money
            return result

    def __repr__(self):
        return f"{self.name},当前剩余金额{self.money}"


class Member(Person):
    students = []

    def grab(self, read_package, num):
        index = random.randint(0, num - 1)
        money = read_package[index]
        self.money += money
        print(f"{self.name}抢到{money}")
        return read_package.pop(index)


if __name__ == '__main__':
    person_num = 3
    member_1 = Member("张三", 10)
    member_2 = Member("李四", 20)
    member_3 = Member("王五", 20)

    manage = Manage("管理员", 20)
    read_packages = manage.send(14, person_num)
    print(manage)

    member_1.grab(read_packages, person_num)
    print(member_1.show())

    member_2.grab(read_packages, person_num - 1)
    print(member_2.show())

    member_3.grab(read_packages, person_num - 2)
    print(member_3.show())

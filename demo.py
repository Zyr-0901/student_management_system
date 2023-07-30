import dataclasses
import os
import sys
import math
import datetime
import logging


def os_demo():
    print("#############")
    print(os.name)
    print(os.path)
    print(os.getcwd())
    # os.mkdir()
    # os.chdir()
    print(os.curdir)


def sys_demo():
    print(sys.path)
    print(sys.argv)
    # sys.exit()


def math_demo():
    math.sin()
    math.cos()
    math.tan()
    math.asin()
    math.acos()
    math.atan()


def datetime_demo():
    print(datetime.datetime.now())
    print(datetime.date.today())
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def log_demo():
    logging.info("info等级")
    logging.warning("warning等级")
    logging.debug("debug等级")
    logging.error("error等级")


def demo(*args):
    print(args)


@dataclasses.dataclass
class Student:
    name: str
    age: int = dataclasses.field(default=20)
    children: list = dataclasses.field(default_factory=list, init=False, repr=False)

    @classmethod
    def cls_name(cls):
        print("类方法")

    @staticmethod
    def sta_name():
        print("静态方法")

    def demo(self):
        print("普通方法")


if __name__ == '__main__':
    # stu = Student("张三")
    # stu.demo()
    # stu.sta_name()
    # stu.cls_name()
    #
    # Student.cls_name()
    # Student.sta_name()

    stu = Student("张三")
    print(stu)
    # print(stu)
    # print(dataclasses.asdict(stu))
    # os_demo()
    # sys_demo()
    # math_demo()
    # datetime_demo()
    # log_demo()
    # a = ["1", "2", "3"]
    # b = "".join(a)
    # print("".join(a))
    # print(b.split(","))
    # a = "fhds fhdsklffhd fhdslaf"
    # b = a.replace("ds", "34")
    # b = [i for i in [2,3,4] if i > 2]
    # print(b)
    # a = {"name": "321", "age": 20}
    # b = a.update({"name": "456", "sex": "男"})
    # print(b)
    # print(a)
    # params = ["python", "java", "php", "go"]
    # demo(*params)
    # a = lambda x: x+1
    # print(a(2))

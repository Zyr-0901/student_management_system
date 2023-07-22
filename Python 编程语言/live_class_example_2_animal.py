class Animal:
    def __init__(self, name: str, color: str, age: int, sex: str):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def can_cry(self):
        print("会叫")

    def can_run(self):
        print("会跑")


class Cat(Animal):
    def __init__(self, name: str, color: str, age: int, sex: str, hair: str):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def __repr__(self):
        return f"猫猫姓名: {self.name},颜色 {self.color},年龄: {self.age}, 性别: {self.sex}, 毛发: {self.hair}, 技能: {self.can_hunt()}"

    def can_hunt(self):
        return "小猫会捕捉老鼠"

    def can_cry(self):
        print("小猫喵喵叫")


class Dog(Animal):
    def __init__(self, name: str, color: str, age: int, sex: str, hair: str):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def __repr__(self):
        return f"狗狗姓名: {self.name},颜色 {self.color},年龄: {self.age}, 性别: {self.sex}, 毛发: {self.hair}"

    def can_cry(self):
        print("小狗汪汪叫")

    def can_house(self):
        print(f"技能: {self.name}会看家")


if __name__ == '__main__':
    cat = Cat("小花猫", "黄色", "2", "女", "短毛")
    print(cat)
    cat.can_cry()

    print("####################################################")
    dog = Dog("二哈", "棕色", "3", "男", "长毛")
    print(dog)
    dog.can_house()

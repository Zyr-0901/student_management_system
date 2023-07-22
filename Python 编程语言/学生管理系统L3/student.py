class Student:
    def __init__(self, stu_id: int, name: str, sex: str):
        self.id = stu_id
        self.name = name
        self.sex = sex

    def __repr__(self):
        return f'学号: {self.id}, 姓名: {self.name}, 性别: {self.sex}'
import student


class StudentManagement:
    """ 学员管理 """

    def __init__(self):
        self.students = []

    def add_student(self, stu):
        self.students.append(stu)


if __name__ == '__main__':
    student_1 = student.Student(1001, "张三", "男")
    student_2 = student.Student(1002, "莉丝", "女")
    student_3 = student.Student(1003, "王武", "男")

    management = StudentManagement()
    management.add_student(student_1)
    management.add_student(student_2)
    management.add_student(student_3)

    print("添加的学员信息：")
    for stu in management.students:
        print(f"学号：{stu.id},姓名：{stu.name},性别：{stu.sex}")

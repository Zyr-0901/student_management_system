import sys
from student import Student
from student_management_execption import StudentManagementExecption
from typing import List


class StudentManagement:
    def __init__(self, students: List[Student]):
        if students:
            self.students = students
        else:
            self.students = []

    def get_student_by_id(self, stu_id: int):
        for stu in self.students:
            if stu.id == stu_id:
                return stu

    def add_student(self, student: Student):
        stu = self.get_student_by_id(student.id)
        if stu:
            print(f"该学员{stu.name}信息已被添加")
        else:
            self.students.append(student)
            print(student)

    def delete_student(self, stu_id: int):
        stu = self.get_student_by_id(stu_id)
        if stu:
            self.students.remove(stu)
            print(f"删除成功,删除的学员信息为:{stu}")
        else:
            print(f"删除失败,学员{stu_id}不存在")

    def get_all_students(self):
        for stu in self.students:
            print(stu)

    def main(self, select_type: int):
        if select_type == 1:
            stu_id = int(input("请输入你要查找的学员编号:"))
            print("学员信息获取成功,该学员信息为:")
            stu = self.get_student_by_id(stu_id)
            print(stu)
        if select_type == 2:
            try:
                stu_id_2 = int(input("请输入学员编号:"))
            except ValueError:
                raise StudentManagementExecption(f"学员名称参数类型错误,必须为整型")

            stu_name_2 = input("请输入学员姓名:")
            stu_sex_2 = input("请输入学员性别:")

            print("学员信添加成功,添加的学员信息为:")
            stu_2_2 = Student(stu_id_2, stu_name_2, stu_sex_2)
            self.add_student(stu_2_2)
        if select_type == 3:
            stu_id_3 = int(input("请输入想要删除的学员编号:"))
            self.delete_student(stu_id_3)
            print("删除后的学员信息为:")
            self.get_all_students()
        if select_type == 4:
            print("所有学员信息如下:")
            self.get_all_students()
        if select_type == 5:
            print("成功退出系统,欢迎下次使用")
            sys.exit()


if __name__ == '__main__':
    stu_1 = Student(1001, "张三", "男")
    stu_2 = Student(1002, "莉丝", "女")
    stu_3 = Student(1003, "王武", "男")
    management = StudentManagement([stu_1, stu_2, stu_3])

    print("-------------欢迎来到学员信息系统----------------")
    print("1.根据学号查看学员信息")
    print("2.添加学员信息")
    print("3.根据学号删除后,查看所有学员信息")
    print("4.查询当前所有学员信息")
    print("5.退出系统")

    select_type = int(input("请输入你的选择:"))
    management.main(select_type)

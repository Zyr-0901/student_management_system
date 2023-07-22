from student import Student
from typing import List


class StudentManagement:
    def __init__(self, students: List[Student]):
        self.students = students

    def get_student(self, stu_id: int):
        for stu in self.students:
            if stu.id == stu_id:
                return stu
            else:
                return False

    def add_student(self, student: Student):
        # 判断是否存在
        # 如果存在则不添加.否则添加
        if self.get_student(student.id):
            print(f"学员: {student.name} 已被添加,无需重复加入")
        else:
            self.students.append(student)
            print(student)

    def delete_student(self, stu_id: int):
        # 判断是否存在,若存在则删除,否则做提醒
        student = self.get_student(stu_id)
        if student:
            print(student)
            return self.students.remove(student)
        else:
            print(f"该学员{student.name}不存在,请确认")
            return False

    def residue_student(self, stu_id: int):
        print("删除的学员信息:")
        self.delete_student(stu_id)
        print("删除后的学员信息:")
        for stu in self.students:
            print(stu)


if __name__ == '__main__':
    student_1 = Student(1001, "张三", "男")
    student_2 = Student(1002, "李四", "女")
    management = StudentManagement([])

    print("添加的学员信息:")
    management.add_student(student_1)
    management.add_student(student_2)
    # 删除学员信息,并打印剩余学员信息
    management.residue_student(1001)
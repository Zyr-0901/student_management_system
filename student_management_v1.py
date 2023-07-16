from typing import List
import student_v1


class StudentManagementV1:
    def __init__(self, students: List[student_v1.StudentV1]):
        if students:
            self.students = students
        else:
            self.students = []

    def _get_student_by_id(self, stu_id: int):
        for stu in self.students:
            if stu.id == stu_id:
                return stu

    def add_student(self, stu: student_v1.StudentV1):
        result = self._get_student_by_id(stu.id)
        if result:
            print(f"该学员已被添加，信息为:\n{stu}")
        else:
            self.students.append(stu)
            print(stu)

    def add_students(self, students: List[student_v1.StudentV1]):
        if students:
            for stu in students:
                result = self._get_student_by_id(stu.id)
                if result:
                    print(f"该学员已被添加，信息为:\n{stu}")
                else:
                    self.students.append(stu)
                    print(stu)


if __name__ == '__main__':
    student_1 = student_v1.StudentV1(1001, "张三", "男")
    # 实例化时同时添加数据
    print("实例化时，添加学员信息：")
    management = StudentManagementV1([student_1])
    print(student_1)

    print("#######################################")

    # 单个学员添加
    print("单个学员添加：")
    student_2 = student_v1.StudentV1(1002, "莉丝", "女")
    management.add_student(student_2)

    print("#######################################")

    # 批量添加
    print("批量学员添加：")
    student_3 = student_v1.StudentV1(1003, "王武", "男")
    student_4 = student_v1.StudentV1(1004, "赵四", "男")
    management.add_students([student_3, student_4])

    print("#######################################")

    # 重复添加
    student_3 = student_v1.StudentV1(1003, "王武", "男")
    management.add_student(student_3)
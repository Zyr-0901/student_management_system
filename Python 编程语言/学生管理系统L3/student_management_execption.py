class StudentManagementExecption(Exception):
    def __init__(self, msg):
        print(f"当前异常为{msg}")



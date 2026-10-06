class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    def StudentInfo(self):
        "name" = self.name
        "age" = self.age
        "id" = self.id
    def add_student(student_list, new_student):
        student_list.append(new_student)
        return student_list
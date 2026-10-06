from Domain import Student, Course, Mark, StudentInfo, CourseInfo, MarkInfo, add_students, add_courses, student_mark
import numpy as np
def input_students():
    all_students = []
    number_Students = int(input("Nhap so luong hs: "))
    for i in range(number_Students):
        print(f"hs thu {i+1}: ")
        name = input("ten: ")
        student_id = input("id hs: ")
        age = int(input("tuoi hs: "))
        st1 = Student(name, age, student_id)
        all_students.append(st1.StudentInfo)
    return all_students
def input_course():
    all_courses = []
    number_courses = int(input("Nhap khoa hoc: "))
    for i in range(number_courses):
        print(f"khoa hoc thu{i+1}: ")
        name = input("ten: ")
        num_of_lessons = int(input("so buoi hoc: ")) 
        course_id = input("ID khoa hoc: ")

        c1 = Course(name, num_of_lessons, course_id)
        all_courses.append(c1.CourseInfo)
    return all_courses

def input_mark():
    table_mark= []
    num_mark = int(input("Nhap so bang diem muon them: "))
    for i in range(num_mark):
        print(f"bang diem thu {i+1}")
        name = input("nhap ten hoc sinh: ")
        course_id = input("nhap id course: ")
        point = input("nhap ten luong diem muon them, viet cach (vd: 7 8 9): ")
        raw_points = point.split()
        raw_points_array = []
        for p in raw_points:
            diem = float(p)
            raw_points_array.append(diem)
        return raw_points_array
    s_avg = float(np.mean[raw_points_array])
    s_sorted = np.sorted(raw_points_array, reverse = True)

    return table_mark, s_avg, s_sorted

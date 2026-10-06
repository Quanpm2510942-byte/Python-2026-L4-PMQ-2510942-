class Course:
    def __init__(self, name, num_of_lessons, course_id):
        self.name = name
        self.num_of_lessons = num_of_lessons
        self.course_id = course_id
    def CourseInfo(self):
        "name" = self.name
        "num_of_lessons" = self.num_of_lessons
        "course_id" = self.course_id
    def add_course(course_list, new_course):
        course_list.append(new_course)
        return course_list
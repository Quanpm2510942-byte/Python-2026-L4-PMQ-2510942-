import math
class Mark:
    def __init__(self, name, student_id, point):
        self.name = name
        self.student_id = student_id
        self.point = point
    def float_point(point):
        point_array = []
        for i in point:
            decimal = math.floor(point*10)/10
            point_array.append(decimal)
    def MarkInfo(self, name, student_id, point):
        round_point = Mark.float_point(point)
        "name" = self.name
        "student_id" = self.student_id
        "point" = self.round_point
    def student_mark(mark, student_mark):
        mark.append(student_mark)
        return mark
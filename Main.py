from Output import display_results
from Input import input_course, input_mark, input_students
def Main():
    ALL_STUDENTS = input.students()
    ALL_COURSE = input.courses()

    table_mark, s_avg, s_sorted = input.mark()

    display_results(table_mark, s_avg, s_sorted)
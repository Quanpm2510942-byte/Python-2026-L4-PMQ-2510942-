print("WARNING, PLEASE INPUT THE DATA IN ORDER")
Students = {}
Courses = {}
Scores = {}


def input_students():
    n = int(input("Students:"))
    for _ in range(n):
        sID = input("Student ID:").strip()
        Name = input("Student name:").strip()
        DoB = input("Student date of birth:").strip()
        Students[sID] = {"Name": Name, "Birthday": DoB}

def input_courses():
    n = int(input("Subjects:"))
    for _ in range(n):
        cID = input("Course ID:").strip()
        CName = input("Course name:").strip()
        Students[cID] = {"Course name": CName}

def Course_Scoring():
    if not Courses:
        print("No courses in list.")
        return
    list_courses()
    cID = input("ID course for mark:").strip()
    if cID not in Courses:
        print("Invalid ID.")
        return

    Scores.setdefault(cID, {})
    for sID, info in Students.items():
        Mark = float(input(f"The score of {info['Name']} ({sID}):"))
        Scores[cID][sID] = Mark

def list_courses():
    print("\n Subjects:")
    if not Courses:
        print("No subjects in list!")
    for cID, info in Courses.items():
        print(f"{cID}-{info['Name']}")

def list_students():
    print("\n List of students:")
    if not Students:
        print("No subjects in list!")
    for sID, info in Students.items():
        print(f"{sID}-{info['Name']}-{info['DoB']}")

def Show_Scores():
    list_courses()
    cID = input("Write score for the course: ").strip()
    if cID not in Courses:
        print("Invalid course ID.")
        return
    if cID not in Scores or not Scores[cID]:
        print("No Scores for this course.")
        return

    print(f"\n mark {Courses[cID]('Name')}")
    for sID, Mark in Scores[cID].items():
        Name = Students.get(sID, ()).get("Name", "Unknown")
        print(f"{sID},{Name}: {Mark}")

def main():
    Actions = {
        "1": input_students,
        "2": input_courses,
        "3": Course_Scoring,
        "4": list_courses,
        "5": list_students,
        "6": Show_Scores,
    }

    menu = "'"
    while True:
        print(menu)
        choice = input("Choose: ").strip()
        if choice == "0":
            break
        Action = Actions.get(choice)
        if Action:
            Action()
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()




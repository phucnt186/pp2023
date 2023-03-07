def inputStudents():
    students = list()
    studentNumber = int(input("Number of students in class: "))
    for i in range(studentNumber):
        id = input(f"Student {i} Id: ")
        name = input(f"Student {i} name: ")
        doB = input(f"Student {i} DoB: ")
        student = {"id": id, "name": name, "doB": doB}
        students.append(student)
    return students

def inputCourses():
    courses = list()
    courseNumber = int(input("Number of courses: "))
    for i in range(courseNumber):
        id = input(f"Course {i} Id: ")
        name = input(f"Course {i} name: ")
        course = {"id": id, "name": name}
        courses.append(course)
    return courses

def inputMarks(course, students):
    mark = list()
    for i in range(len(students)):
        m = input(f"{students[i]['name']}'s {course['name']}")
        mark.append(m)
    return mark

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # data
    students = inputStudents()
    courses = inputCourses()
    courseMarks = list()
    for i in range(len(courses)):
        m = list()
        for j in range(len(students)):
            m.append(0)
        courseMarks.append(m)
    print(courseMarks)

    while(True):
        print("Enter the number to choose a function")
        print("1. List courses")
        print("2. List students")
        print("3. Input student marks for a given course")
        print("4. Show student marks for a given course")
        print("5. Exit")
        i = input("Your choice: ")
        if(i=='1'):
            print("list course")
            print(courses)
        elif(i=='2'):
            print("List student")
            print(students)
        elif(i=='3'):
            print("3. Input student marks for a given course")
            for cid in range(len(courses)):
                print(f"{cid}. {courses[cid]['name']} ")
            cid = int(input("Choose course: "))
            courseMarks[cid] = inputMarks(courses[cid], students)
        elif(i=='4'):
            print("Student marks")
            while(True):
                print("Select course")
                for course in courses:
                    print(course["id"], course["name"])
                selectedCourseId = input("Select course id: ")
                for course in courses:
                    if(selectedCourseId == course["id"]):
                        print(course)
        elif(i=='5'):
            break
        else:
            print("Choose the right number. plz")

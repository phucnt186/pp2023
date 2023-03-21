ls_student = []
ls_course = []

class Student:
    def __init__(self, studentID, studentName, studentDob):
        self.id = studentID
        self.name = studentName
        self.dob = studentDob
        self.marks = {}

# Encapsulation
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getDob(self):
        return self.dob
    
    def getMark(self):
        return self.marks
    
    def setID(self, _id):
        self.id = _id

    def setName(self, name):
        self.name = name

    def setDob(self, dob):
        self.dob = dob

    def setMark(self, course, mark):
        self.mark({course: mark}) # Maybe I should overlook at this?

    def displayStudent(self):
        print("Student ID: " + self.id)
        print("Name: " + self.name)
        print("Date of birth: " + self.dob)

    def displayMark(self, course):
        print(self.name + "mark: " + str(self.marks.get(course))) # later

class Course:
    def __init__(self, courseID, courseName):
        self.id = courseID
        self.name = courseName

    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def setID(self, _id):
        self.id = _id

    def setName(self, name):
        self.name = name

    def displayCourse(self):
        print("Code: " + self.id)
        print("Subject: " +self.name)
# End class

def studentNum():
    studentNum = int(input("Enter number of student: "))
    return studentNum

def inputStudent():
    studentID = input("Student ID: ")
    studentName = input("Name: ")
    studentDob = input("Date of birth: ")
    return studentID, studentName, studentDob

def courseNum():
    courseNum = int(input("Enter the number of course: "))
    return courseNum

def inputCourse():
    courseID = input("Code: ")
    courseName = input("Subject: ")
    return courseID, courseName

def findCourse(course, courseID):
    for course in ls_course:
        if course.getID() == courseID:
            return course.getName()
        else:
            print("Invalid ID!")

# Main
if __name__ == "__main__":

    studentNum = studentNum()
    print(studentNum)
    for i in range(0, studentNum):
        id, name, dob = inputStudent()
        ls_student.append(Student(id, name, dob))

    courseNum = courseNum()
    for i in range(0, courseNum):
        id, name = inputCourse()
        ls_course.append(Course(id, name))

    print("Show student information:\n")
    for student in ls_student:
        student.displayStudent()

    print("Show course information:\n")
    for course in ls_course:
        course.displayCourse()

    a = 'b'
    while a == 'b':
        selectCourseID = ("Enter subject code: ")
        selectCourse = findCourse(ls_course, selectCourseID)
        print("Course name: " + selectCourse + "\n")

        for student in ls_student:
            mark = input("Enter " + student.name + "mark: ")
            student.setMark(selectCourse, mark)
        
        a = input("Choose another course? (y/N): ")

        selectCourseID = input("Choose an existed course ID: ")
        selectCourse = findCourse(ls_course, selectCourseID)
        print(f"Display student's mark of course {selectCourse}: \n")

        for student in ls_student:
            student.displayMark(selectCourse)
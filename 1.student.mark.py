# Create a list to add student
ls_student = {}

# Create a list to add course
ls_course = []

# Create a list to add mark
ls_mark = []

# Enter student infomation
def inputStudent():
    studentNum = int(input("Enter the number of students in class: "))
    for i in range(studentNum):
        studentID = input("Student ID: ")
        studentName = input("Name: ")
        studentDob = input("Date of birth: ")
        ls_student[studentID] = {'name': studentName, 'dob': studentDob}

# Enter course infomation
def inputCourse():
    courseNum = int(input("\nEnter the number of course: "))
    for i in range(courseNum):
        courseID = input("Code: ")
        courseName = input("Subject: ")
        ls_course[courseID] = {'name': courseName}

# Enter student's mark for a course
def inputMark():
    # Choose course to enter student's mark
    courseID = input("Enter subject code: ")
    if courseID not in ls_course:
        print("Invalid code")
    # Enter student mark
    for studentID in ls_student:
        studentMark = float(f"Enter {ls_student[studentID]['name']}'s mark:")
        if studentID not in studentMark:
            studentMark[studentID] = {}
        studentMark[studentID][courseID] = studentMark

# Display list of students
def displayStudent():
    for studentID in ls_student:
        print(f"{studentID}    {ls_student[studentID]['name']}    {ls_student[studentID]['dob']}\n")

# Display list of courses
def displayCourse():
    for courseID in ls_course:
        print(f"{courseID}    {ls_course[courseID]['name']}") # something wrong with this?

# Display the student mark
def displayMark(self, course):
    courseID = input("Enter subject code: ")
    if courseID not in ls_course:
        print("Invalid code")
    for studentID in ls_student:
        if studentID in ls_mark and courseID in ls_mark[studentID]:
            print(f"{ls_student[studentID]['name']}: {ls_mark[studentID][courseID]}")
        else:
            print(f"{ls_student[studentID]['name']}: NULL")

# Main
inputStudent()
inputCourse()

while True:
    print("\nEnter the number to choose a function")
    print("1. List students")
    print("2. List courses")
    print("3. Select a course") # Input mark here
    print("4. List student's mark")
    
    choice = input("Your choice: ")

    if(choice == '1'):
        print("\nList student:")
        displayStudent()
    elif(choice == '2'):
        print("\nList course:")
        displayCourse()
    elif(choice == '3'):
        inputMark()
    elif(choice == '4'):
        displayMark()
    else:
        print("Invalid choice!")

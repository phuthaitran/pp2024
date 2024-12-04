def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return (student_id, student_name, student_dob)

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return (course_id, course_name)

def input_marks_for_course(students):
    marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student[1]} (ID: {student[0]}): "))
        marks[student[0]] = mark
    return marks

def show_courses(courses):
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def show_students(students):
    print("List of students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}")

def show_marks_in_course(students, marks, course_id):
    print(f"Student marks for course ID {course_id}:")
    for student in students:
        if student[0] in marks[course_id]:
            print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}, Mark: {marks[course_id][student[0]]}")
        else:
            print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}, Mark: Not available")

students = []
courses = []
marks = {}

num_students = input_number_of_students()
for _ in range(num_students):
    student_info = input_student_info()
    students.append(student_info)

num_courses = input_number_of_courses()
for _ in range(num_courses):
    course_info = input_course_info()
    courses.append(course_info)
    marks[course_info[0]] = {}  

while True:
    print("\nMenu:")
    print("1. Add students")
    print("2. Add courses")
    print("3. List students")
    print("4. List courses")
    print("5. Select a course and input marks for students")
    print("6. Show student marks for a course")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        num_students = input_number_of_students()
        for _ in range(num_students):
            student_info = input_student_info()
            students.append(student_info)
    elif choice == 2:
        num_courses = input_number_of_courses()
        for _ in range(num_courses):
            course_info = input_course_info()
            courses.append(course_info)
            marks[course_info[0]] = {}
    elif choice == 3:
        show_students(students)
    elif choice == 4:
        print("List of courses:")
        show_courses(courses)
    elif choice == 5:
        print("List of courses to choose from:")
        show_courses(courses)
        course_id = input("Enter course ID to enter marks: ")
        if course_id in marks:
            print(f"Entering marks for course {course_id}:")
            course_students = [student for student in students]
            marks[course_id] = input_marks_for_course(course_students)
        else:
            print("Invalid course ID")
    elif choice == 6:
        print("List of courses to choose from:")
        show_courses(courses)
        course_id = input("Enter course ID to show marks: ")
        if course_id in marks:
            show_marks_in_course(students, marks, course_id)
        else:
            print("Invalid course ID")
    elif choice == 7:
        break
    else:
        print("Invalid choice. Please enter a valid option.")

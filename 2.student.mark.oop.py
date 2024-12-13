class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @property
    def dob(self):
        return self.__dob

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, DOB: {self.__dob}"


class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name
        self.__marks = {}

    @property
    def course_id(self):
        return self.__course_id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"ID: {self.__course_id}, Name: {self.__name}"
    
    def add_marks(self, student_id, mark):
        self.__marks[student_id] = mark

    def show_marks(self, students):
        print(f"Student marks for course ID {self.__course_id}:")
        for student in students:
            if student.student_id in self.__marks:
                print(f"{student}, Mark: {self.__marks[student.student_id]}")
            else:
                print(f"{student}, Mark: Not available")


class Input:
    def __init__(self):
        self.__students = []
        self.__courses = []

    @property
    def students(self):
        return self.__students

    @property
    def courses(self):
        return self.__courses

    def input_number_of_students(self):
        return int(input("Enter the number of students: "))

    def input_student_info(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        return Student(student_id, name, dob)

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_info(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        return Course(course_id, name)

    def input_marks_for_course(self, course_id):
        course = next((c for c in self.__courses if c.course_id == course_id), None)
        if not course:
            print("Invalid course ID")
            return

        for student in self.__students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
            course.add_marks(student.student_id, mark)


class Display:
    @staticmethod
    def show_students(students):
        if not students:
            print("Student list is empty!")
        else: 
            print("List of students:")
            for student in students:
                print(student)

    @staticmethod
    def show_courses(courses):
        if not courses:
            print("Course list is empty!")
        else:
            print("List of courses:")
            for course in courses:
                print(course)

    @staticmethod
    def show_marks_in_course(course, students):
        course.show_marks(students)


def menu(school):
    display_manager = Display()

    while True:
        print("\nMenu:")
        print("1. List students")
        print("2. List courses")
        print("3. Add students")
        print("4. Add courses")
        print("5. Select a course and input marks for students")
        print("6. Show student marks for a course")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            display_manager.show_students(school.students)
        elif choice == '2':
            display_manager.show_courses(school.courses)
        elif choice == '3':
            num_students = school.input_number_of_students()
            for _ in range(num_students):
                school.students.append(school.input_student_info())
        elif choice == '4':
            num_courses = school.input_number_of_courses()
            for _ in range(num_courses):
                school.courses.append(school.input_course_info())
        elif choice == '5':
            if not school.students:
                print("Student list is empty. Cannot enter the marks.")
            elif not school.courses:
                print("There is no course to choose from!")
            else:
                display_manager.show_courses(school.courses)
                course_id = input("Enter course ID to enter marks: ")
                school.input_marks_for_course(course_id)
        elif choice == '6':
            if not school.students:
                print("Student list is empty. Cannot view the marks.")
            elif not school.courses:
                print("There is no course to choose from!")
            else:
                display_manager.show_courses(school.courses)
                course_id = input("Enter course ID to show marks: ")
                course = next((c for c in school.courses if c.course_id == course_id), None)
                if course:
                    display_manager.show_marks_in_course(course, school.students)
                else:
                    print("Invalid course ID")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    school = Input()
    menu(school)

"""  Add students from the user input student name and grade
Save students in a file called grades.txt.
Use exception handling to block errors if user enter wrong values.
Create a function for viewing students
Read and Print students and their grades from the file.
Create a function for searching a student
asks  a user to enter a name search the file for that name and print their
 grade
handle the error if student is not found
use a loop to display a menu for a to select from for whatever they want to do
call an appropriate function based on the user choice
handle invalid menu choies with exceptions or simple error handling. """


class StudentNotFoundError(Exception):
    pass


def add_student(filename):

    # Ask user to input student name and grade
    student_name = input("please enter student name: ")
    try:
        student_grade = int(input("please enter student grade from 1-12: "))
        if student_grade < 0 or student_grade > 12:
            raise ValueError("Grade must be between 1 and 12")
            # Create and Add user input to a file
        with open(filename, 'a') as file:
            file.write(f"{student_name}, {student_grade} \n")
    except ValueError:
        print("you have entered an invalid grade")


def view_student(filename):
    try:
        with open(filename, "r") as file:
            contents = file.read()
            if contents:
                print(contents)
            else:
                print("contents are not found")
    except FileNotFoundError:
        print("file not found")


def search_student(filename, search_name):
    try:
        with open(filename, "r") as file:
            for line in file:
                student_name, student_grade = line.strip().split(",")
                if student_name.lower() == search_name.lower():
                    return student_grade
        raise StudentNotFoundError(f"The {search_name} is not found")
    except FileNotFoundError:
        print("no data yet, please add students first")
    except StudentNotFoundError:
        print("The student is not found")


def main():
    filename = "grade.txt"
    while True:
        print("\n Menu:")
        print("1. Add student")
        print("2. Search student")
        print("3. view student")
        print("4. exit")

        try:
            choice = int(input("enter your choice: "))
            if choice == 1:
                add_student(filename)
            elif choice == 2:
                name = input("please enter the name of the student: ")
                grade = search_student(filename, name)
                if grade:
                    print(f"{name}'s grade is {grade}")
            elif choice == 3:
                view_student(filename)
            elif choice == 4:
                print("exiting program")
                break
        except ValueError as e:
            print(e)


main()

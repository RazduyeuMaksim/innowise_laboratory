from typing import Optional, List, Union

StudentType = dict[str, Union[str, List[int]]]
students: List[StudentType] = []


def get_student_name() -> str:
    """
    Prompts the user for a student name.
    Trims extra whitespace.
    """
    return input("Enter student name: ").strip()


def get_student_grade() -> str:
    """
    Prompts the user for a grade, removes extra whitespace.
    Handles the 'done' command for ending the input process.
    """
    return input("Enter a grade (or 'done' to finish): ").strip()


def check_student_in_list(student_name: str) -> bool:
    """
    Checks if a student with the given name exists in the students list.
    """
    return any(
        student["name"].casefold() == student_name.casefold() for student in students
    )


def get_student_by_name(student_name: str) -> Optional[StudentType]:
    """
    Function searches for a student in the list by name
    and returns the student's data as a dictionary if found,
    otherwise returns None
    """
    for student in students:
        if student_name.casefold() == student["name"].casefold():
            return student
    return None


def calculate_average(student: StudentType) -> Optional[float]:
    """
    Function takes a student dictionary
    and calculates the average grade.
    If the student has no grades, it returns None.
    """
    student_grades: List[int] = student["grades"]
    try:
        average_grade: float = sum(student_grades) / len(student_grades)
    except ZeroDivisionError:
        return None
    return average_grade


def check_student_name(student_name: str) -> bool:
    """
    Validates the student's name:
    1. The name cannot be empty.
    2. The student with this name must not already exist in the list.
    Returns True if the name is valid, otherwise False.
    """
    if len(student_name) == 0:
        print("Student name cannot be empty")
        return False

    if check_student_in_list(student_name):
        print(f"The student {student_name} already exists.")
        return False

    return True


def check_student_grade(student_grade_str: str) -> Optional[int]:
    """
    This function validates a student's grade.
    First, it tries to convert the input string to an integer.
    If conversion fails, it prints an error message and returns None.
    Then it checks that the number is within the range 0 to 100.
    If the number is out of range, it also returns None.
    If everything is valid, it returns the grade as an integer.
    """
    try:
        student_grade: int = int(student_grade_str)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

    if not (0 <= student_grade <= 100):
        print("Invalid input. Please enter a number from 0 to 100.")
        return None

    return student_grade


def add_student() -> None:
    """
    This function adds a new student to the students list.
    It first prompts for the student's name and validates it.
    If the name is valid, it creates a dictionary with the name
    and an empty grades list,
    then appends it to the main students list.
    """
    student_name: str = get_student_name()

    if not check_student_name(student_name):
        return

    student_dict: StudentType = {"name": student_name, "grades": []}

    students.append(student_dict)


def add_grade() -> None:
    """
    Function to add a grade for a student.
    First, it prompts for the student's name.
    If the student exists in the list, it allows entering grades until 'done' is entered.
    Each valid grade is appended to the student's grade list.
    If the student is not found, a message is displayed.
    """
    student_name: str = get_student_name()

    if check_student_in_list(student_name):
        while True:
            student_grade_str: str = get_student_grade()
            if student_grade_str.lower() == "done":
                break
            else:
                student_grade: Optional[int] = check_student_grade(student_grade_str)

                if student_grade is None:
                    continue

                student: Optional[StudentType] = get_student_by_name(student_name)
                student_grades: List[int] = student["grades"]
                student_grades.append(student_grade)
    else:
        print(f"Student {student_name} not found.")


def show_report() -> None:
    """
    Function prints a report of all students.
    For each student, it calculates the average grade.
    If there are no grades, it displays "N/A".
    It also collects all numeric average values to calculate the maximum, minimum, and overall average grades.
    If there is no students, appropriate message is displayed.
    """
    average_list: List[float] = []

    print(f"--- Student Report ---")
    if not students:
        print("No students.")
        return

    for student in students:
        average_value: Optional[float] = calculate_average(student)

        if average_value is not None:
            average_list.append(round(average_value, 2))
        else:
            average_value: str = "N/A"

        print(f"{student['name']}'s average grade is {average_value}.")

    average_list_nums: List[float] = [
        number for number in average_list if isinstance(number, (int, float))
    ]

    if not average_list_nums:
        return

    print(f"--------------------------")
    print(f"Max Average: {max(average_list_nums)}")
    print(f"Min Average: {min(average_list_nums)}")
    print(f"Overall Average: {sum(average_list_nums)/len(average_list_nums)}")


def top_performer() -> None:
    """
    This function finds the student with the highest average grade.
    If no student has valid grades, it prints a message indicating this.
    Otherwise, it prints the student's name along with their average grade.
    """
    if not students:
        print(f"No students.")
        return

    student_with_grades: List[StudentType] = list(
        filter(lambda student: calculate_average(student) is not None, students)
    )

    if not student_with_grades:
        print("No students with valid grades to determine a top performer")
        return

    top_student: StudentType = max(
        student_with_grades, key=lambda student: calculate_average(student)
    )

    print(
        f"The student with the highest average is {top_student['name']} with the grade of {calculate_average(top_student)}."
    )


def exit_program() -> None:
    """
    Exits the program.
    """
    print(f"Exiting program.")


def handle_command(command: int) -> bool:
    """
    This function handles the user's command by calling the corresponding function for each menu option.
    If the user selects "5", the program exits and returns False.
    """
    match command:
        case 1:
            add_student()
        case 2:
            add_grade()
        case 3:
            show_report()
        case 4:
            top_performer()
        case 5:
            exit_program()
            return False
        case _:
            print("Invalid choice. Please select a number from 1 to 5.")
    return True


def display_menu() -> None:
    """
    This function displays the main menu of the program.
    """
    print(f"--- Student Grade Analyzer ---")
    print(f"1. Add a new student")
    print(f"2. Add grades for a student")
    print(f"3. Generate a full report")
    print(f"4. Find the top student")
    print(f"5. Exit program")


def get_user_choice() -> str:
    """
    Retrieves the user's choice from input.
    Strips any extra spaces.
    """
    return input("Enter your choice: ").strip()


def check_user_choice(user_choice: str) -> Optional[int]:
    """
    Function tries to convert the user's input into an integer.
    If the input is invalid (not a number), it prints an error message and returns None.
    """
    try:
        return int(user_choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def main() -> None:
    """
    Main function of the program that runs an infinite menu loop.
    The user selects an action, the choice is validated, and the corresponding command is executed.
    The loop continues until exit.
    """
    while True:
        try:
            display_menu()
            user_choice: Optional[int] = check_user_choice(get_user_choice())
            if user_choice is not None:
                if not handle_command(user_choice):
                    break
        except KeyboardInterrupt:
            print("Interrupted by user.")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

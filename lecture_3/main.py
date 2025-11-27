def determining_student_with_top_average(STUDENTS: list) -> {str, float}:
    # A function for determining students with highest average
    max_average = calculate_max_average(STUDENTS)
    if isinstance(max_average, str):
        return 'There is no grade!'
    for student in STUDENTS:
        if student.get('average_grade') == max_average:
            return {'name': student.get('name'), 'average_grade': student.get('average_grade')}


def calculate_overall_average(STUDENTS: list) -> float | str:
    # A function for determining overall average grade between STUDENTS
    average_grades = []
    sum_average_grades = 0
    for student in STUDENTS:
        if isinstance(student.get('average_grade'), (int, float)):
            average_grades.append(student.get('average_grade'))
            sum_average_grades += student.get('average_grade')
    if not average_grades:
        return 'N/A'
    overall_average_grade = sum_average_grades / len(average_grades)
    return overall_average_grade


def calculate_max_average(STUDENTS: list) -> float | str:
    # A function for determining max average grade between STUDENTS
    average_grades = []
    for student in STUDENTS:
        if isinstance(student.get('average_grade'), (int, float)):
            average_grades.append(student.get('average_grade'))
    if not average_grades:
        return 'N/A'
    return max(average_grades)


def calculate_min_average(STUDENTS: list) -> float | str:
    # A function for determining min average grade between STUDENTS
    average_grades = []
    for student in STUDENTS:
        if isinstance(student.get('average_grade'), (int, float)):
            average_grades.append(student.get('average_grade'))
    if not average_grades:
        return 'N/A'
    return min(average_grades)


def calculate_average_grade(grades: list) -> float | str:
    # This function calculates the average value
    # of a student's grade list and returns a number
    if not grades:
        return 'N/A'
    average_grade = 0
    count_grade = len(grades)
    for grade in grades:
        average_grade += grade
    average_grade = average_grade/count_grade
    return average_grade


def main():
    # List for store information about student in dictionaries
    STUDENTS = []

    while (True):
        print('''
--- Student Grade Analyzer ---
1. Add a new student
2. Add grades for a student
3. Generate a full report
4. Find the top student
5. Exit program
             ''')

        answer = input('Enter your choice: ')
        match answer:
            case '1': 
                name_added_user = input('Enter student name: ')
                STUDENTS.append({'name': name_added_user})
            case '2':
                while (True):
                    name_select_user = input('Enter student name: ')
                    is_user_found = False
                    for student in STUDENTS:
                        if student.get('name') == name_select_user:
                            is_user_found = True
                    if is_user_found:
                        break
                    else:
                        print('The user does`t exist')

                grades = []
                while (True):
                    grade_answer = input("Enter a grade (or 'done' to finish): ")

                    if grade_answer == 'done':
                        break

                    try:
                        grades.append(int(grade_answer))
                    except ValueError:
                        print('Invalid input. Please enter a number.')
                    except Exception as e:
                        print(e)

                for student in STUDENTS:
                    if student.get('name') == name_select_user:
                        student.setdefault('grades', grades)
            case '3':
                report_string = '--- Student Report ---\n'

                for student in STUDENTS:
                    student.setdefault('average_grade', calculate_average_grade(student.get('grades')))
                    report_string += f"{student.get('name')}`s average grade is {student.get('average_grade')}\n"
                report_string += '----------------------\n'
                report_string += f'Max Average: {calculate_max_average(STUDENTS)}\n'
                report_string += f'Min Average: {calculate_min_average(STUDENTS)}\n'
                report_string += f'Overall Average: {calculate_overall_average(STUDENTS)}\n'
                print(report_string)
            case '4':
                result = determining_student_with_top_average(STUDENTS)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f'The student with the highest average is {result.get('name')} with a grade of {result.get('average_grade')}\n')
            case '5':
                print('Exit')
                break
            case _:
                print('Invalid input!')


if __name__ == "__main__":
    main()

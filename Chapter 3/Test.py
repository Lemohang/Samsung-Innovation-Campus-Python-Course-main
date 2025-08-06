from Student import Student

def main():
    print("======== Student Details ==========")
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    
    student = Student(name, student_id)

    
    eng_quiz = list(map(int, input("Enter English quiz scores separated by spaces: ").split()))
    student.set_eng_quiz(eng_quiz)

    
    math_quiz = list(map(int, input("Enter Math quiz scores separated by spaces: ").split()))
    student.set_math_quiz(math_quiz)

    
    science_quiz = list(map(int, input("Enter Science quiz scores separated by spaces: ").split()))
    student.set_science_quiz(science_quiz)

    print("\nStudent Information:")
    print(student)
    print("Total Score:", student.get_total_score())
    print("Average Score:", student.get_avg_score())

if __name__ == "__main__":
    main()





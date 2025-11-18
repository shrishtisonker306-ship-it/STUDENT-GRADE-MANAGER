# Student Grade Manager

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def add_student(students):
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / num_subjects
    grade = calculate_grade(percentage)

    students.append({
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })

    print(f"\nRecord added for {name}!")
    print(f"Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}\n")

def view_students(students):
    if not students:
        print("\nNo records found.\n")
        return

    print("\n===== Student Records =====")
    print(f"{'Name':<15}{'Total':<10}{'Percentage':<15}{'Grade':<5}")
    print("-" * 45)

    for s in students:
        print(f"{s['name']:<15}{s['total']:<10}{s['percentage']:<15.2f}{s['grade']:<5}")
    print()

def main():
    students = []

    while True:
        print("=== Student Grade Manager ===")
        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()

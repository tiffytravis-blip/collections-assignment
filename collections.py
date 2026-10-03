def letter_grades(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


student_name = input("Enter the student name: ")

grade1 = float(input("Enter grade : "))
grade2 = float(input("Enter grade : "))
grade3 = float(input("Enter grade : "))
grade4 = float(input("Enter grade : "))
grade5 = float(input("Enter grade : "))

average = (grade1 + grade2 + grade3 + grade4 + grade5) / 5

letter_grade = letter_grades(average)

print(student_name)
print("Average:", average)
print("Letter Grade:", letter_grade)
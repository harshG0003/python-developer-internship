
def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"
    return average, grade
marks = []

for i in range(5):
    mark = float(input("Enter marks out of 100: "))

    if mark < 0 or mark > 100:
        print("Invalid marks. Run the program again.")
        break
    marks.append(mark)

if len(marks) == 5:
    average, grade = calculate_grade(marks)
    print("Average marks:", average)
    print("Grade:", grade)

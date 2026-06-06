import csv

with open('grades.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

grade_sum = 0
count = 0
highest_grade = 0
highest_student = ""
lowest_grade = 100
lowest_student = ""

for row in data:
    student = row[0]
    grade = float(row[1])
    if grade > highest_grade:
        highest_grade = grade
        highest_student = student
    if grade < lowest_grade:
        lowest_grade = grade
        lowest_student = student
    grade_sum += grade
    count += 1

average_grade = grade_sum / count
grades_below_average = 0
grades_above_average = 0

for row in data:
    grade = float(row[1])
    if grade > average_grade:
        grades_above_average += 1
    elif grade < average_grade:
        grades_below_average += 1

percentage_above_average = grades_above_average / count * 100
percentage_below_average = grades_below_average / count * 100

print("Average: " + str(average_grade))
print("Maximum: " + str(highest_grade) + "(" + highest_student + ")")
print("Minimum: " + str(lowest_grade) + "(" + lowest_student + ")")
print("Grades above average: " + str(grades_above_average) + ", " + str(percentage_above_average) + "%")
print("Grades below average: " + str(grades_below_average) + ", " + str(percentage_below_average) + "%")





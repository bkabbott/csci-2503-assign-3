import csv

# Open CSV file and add it to a list
with open('grades.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

# Declare and set variables
grade_sum = 0
count = 0
highest_grade = None
highest_student = ""
lowest_grade = None
lowest_student = ""
grades_below_average = 0
grades_above_average = 0

# Iterate through list first time to calculate the highest grade, the lowest grade, and the sum
for row in data:
    student = row[0]
    grade = float(row[1])
    if highest_grade is None or grade > highest_grade:
        highest_grade = grade
        highest_student = student
    if lowest_grade is None or grade < lowest_grade:
        lowest_grade = grade
        lowest_student = student
    grade_sum += grade
    count += 1

# Calculate average grade
average_grade = grade_sum / count

# Iterate through list a second time to calculate grades above and below the average grade
for row in data:
    grade = float(row[1])
    if grade > average_grade:
        grades_above_average += 1
    elif grade < average_grade:
        grades_below_average += 1

# Calculate the percentages above or below the average
percentage_above_average = grades_above_average / count * 100
percentage_below_average = grades_below_average / count * 100

# Display output to user
print("Average: " + str(average_grade))
print("Maximum: " + str(highest_grade) + " (" + highest_student + ")")
print("Minimum: " + str(lowest_grade) + " (" + lowest_student + ")")
print("Grades above average: " + str(grades_above_average) + ", " + str(percentage_above_average) + "%")
print("Grades below average: " + str(grades_below_average) + ", " + str(percentage_below_average) + "%")





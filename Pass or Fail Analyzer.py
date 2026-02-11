'''Problem Statement:
Analyze student results.
marks = [45, 78, 90, 33, 60]

Requirements:
A student passes if marks ≥ 50
Count the total number of pass students
Count the total number of fail students
Print the final result clearly
Real-World Application: Academic evaluation systems
'''

marks = [45, 78, 90, 33, 60]
n = len(marks)
Passcount = 0
Failcount = 0
for i in range(n):
    if marks[i] >= 50:
        Passcount = Passcount + 1
    else:
        Failcount = Failcount + 1
print("Total number of students passed: ", Passcount)
print("Total number of studetns failed: ", Failcount)


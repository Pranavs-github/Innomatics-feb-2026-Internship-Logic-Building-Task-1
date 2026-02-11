'''Problem Statement:
Detect error messages from system logs.
logs = ["INFO", "ERROR", "WARNING", "ERROR"]

Requirements:
Count the number of "ERROR" entries
Print the total error count
Real-World Application: Monitoring and log analysis systems
'''

logs = ["INFO", "ERROR", "WARNING", "ERROR"]
n = len(logs)
count = 0
for i in range(n):
    if logs[i] == "ERROR":
        count = count + 1
print("Total number of error counts:", count)
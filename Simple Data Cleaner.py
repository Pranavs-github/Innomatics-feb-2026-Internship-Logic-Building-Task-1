'''Problem Statement:
Clean and standardize user names.
names = [" Alice ", "bob", " CHARLIE "]

Requirements:
Remove extra spaces
Convert all names to lowercase
Print the cleaned list
Real-World Application: Data preprocessing before analysis
'''

names = [" Alice ", "bob", " CHARLIE "]
n = len(names)
Names = []

for i in range(n):
    Names.append(names[i].strip().lower())
print(Names)
    
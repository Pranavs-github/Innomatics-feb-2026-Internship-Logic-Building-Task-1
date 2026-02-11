print("jai shri ram")
'''Problem Statement:
Given a username and password, check whether login is successful.
username = "admin"
password = "1234"

Requirements:
Print "Login Successful" if both username and password match
Otherwise print "Invalid Credentials"
Real-World Application: Authentication systems
'''

username = input("Enter the username: ")
password = input("Enter the password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")
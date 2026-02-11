'''Problem Statement:
Analyze message sizes.
messages = ["Hi", "Welcome to the platform", "OK"]

Requirements:
Print the length of each message
Flag messages longer than 10 characters
Real-World Application: Text filtering and validation systems
'''

messages = ["Hi", "Welcome to the platform", "OK"]
n = len(messages)
flag = False

for i in range(n):
    print("The length of the message: ", messages[i],"=>", len(messages[i]))
    
    if len(messages[i]) > 10:
        flag = True
        print("flagging the message bcz length longer then 10 characters", flag)
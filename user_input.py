def user_input():
    userName = input("Enter your name: ")
    if len(userName) >= 3:
        result = 'Hello <<UserName>>, How r u?'
        result1 = result.replace("UserName", userName)
        print(result1)
user_input()
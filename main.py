import include # function include 

# print hello
print("hello world!")

# user enter name
name = input("Enter your name: ")

# user enter age
age = int(input("Enter your age: "))

# return info
user = include.user_info(name, age)
print(user)

# check user age
user_age = include.check_age(age)
print(user_age)



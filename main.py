from include import user_info, check_age # function include 

# print hello
print("hello world!")

try:
	# user enter name
	name = input("Enter your name: ")

	# user enter age
	age = int(input("Enter your age: "))
except ValueError:
	print("Please provide valid input")
	exit(0)

# return info
user = user_info(name, age)
print(user)

# check user age
user_age = check_age(age)
print(user_age)



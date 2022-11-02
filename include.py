# Return user data
def user_info(name="oh", age=0):
    return f"Yeah, your name is: {name}, and your age is: {age}!"


# Ckeck Age
def check_age(age=0):
    print(f"> Your age is: {age}")
    if age >= 18:
        return f"> Okay you can entry"
    else:
        return f"> Sorry you can not entry"



# Let's create a while loop
# break and continue are key words that we can use to control the flow of our program
# Syntax: while variable_name condition value:
# number = 0
#
# while number < 10:
#     print(f"it's working -> {number}")
#     if number == 5:
#         break
#     number += 1
#

# take user input with while loop

user_prompt = True

while user_prompt:
    age = input("Please enter your age? ")
# Note this user input is within our while therefore it'll prompt the user until we get desired input

    if age.isdigit() and int(age) < 117:
    # isdigit() checks if the input is all digits

        user_prompt = False
    else:
        print("Please provide age in digits")

print(f"Your age is {age}")











# num = 0
#
# while num < 10:
#     print(f"it's working -> {num}")
#     if num == 4:
#         break
#     num += 1














# user_prompt = True



# while user_prompt:
#     age = input("Please enter your age ")
#     if age.isdigit() and int(age) < 117: # isdigit to stop users entering string
#         user_prompt = False
#     else:
#         print("Please answer in numbers")
# print(f"Your age is {age}")
#
# def greet_user(name):
#     print("welcome Dear " + name)
# greet_user("shahrukh")
#
# def add(num1, num2):
#     return num1 + num2
#
# total = add(2, 3)
# print(total)
#
# # classes
#
# class Dog:
#     animal_kind = "canin"
#
#     def bark(self):
#         self.animal_kind
#         return "woof"
# fido = Dog()
#
# lassi = Dog()
#
# print(Dog.animal_kind)
# print(type(fido.animal_kind))
# print(type(lassi.bark()))
#
# fido.animal_kind = "Big Dog"
# print(fido.animal_kind)
# print(lassi.animal_kind)
# Loops for Loop and while loop
# for Loop is used to iterate through the data
# Syntax for variable_name in name_of_data_collection_variable

shopping_list = ["eggs", "milk", "super malt"]
#print(shopping_list)

for items in shopping_list:
    if items == "milk":
        print(items)




# for items in shopping_list:
#     if items == "milk":
#         print(items)
#         break

# for items in shopping_list:
#     if items == "milk":
#         print(items)
# from datetime import date
#
# # gathering user data
# name = input("What is your name? ").title()
# age = int(input("How old are you? "))
# not_had_bday = True if input("Have you had your birthday yet? (y/n) ") == 'n' else False
#
# # calculate birthyear considering whether they've had their birthday or not
# birthyear = date.today().year - age - not_had_bday
#
# # message to user
# print(f"Hi {name}, you are {age} years old, you were born in {birthyear}. You've been alive for a minimum of {age*365*24} hours")

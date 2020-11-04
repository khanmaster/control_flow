# This lesson will cover control flow
## if statements, elif, and else statements
### for loops and while loops

- While loops is not regularly use however you do see it being used for monitoring 
- We have a key-words ```break``` and ```continue``` that help control the flow of our loop


- Let's create a while loop
- ```break``` and ```continue``` are ```key-words``` that we can use to control the flow of our program
- Syntax: ```while variable_name condition value:```
```
number = 0

while number < 10:
     print(f"it's working -> {number}")
     if number == 5:
         break
     number += 1
```

- Take user input with while loop
```
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
```

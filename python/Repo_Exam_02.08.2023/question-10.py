# 1-creat a python function named print_message that takes a parameter message and a parameter repeat_count, where repear_count has a defult value of 1.
# 2- The function should print the message the number of times specified by repear_count.
# 3- Prompt the userto enter a message and a repeat count(optinal).
# 4- Call the print_message function width the user-privided values or using the default value.



def print_message(message, repeat_count=1):

  for x in range(repeat_count):
    print(message)



message = input("Hi_Wellcme to the this Office)")
repeat_count = input("What is your post name: ")
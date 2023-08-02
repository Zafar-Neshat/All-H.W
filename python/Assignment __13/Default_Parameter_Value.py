"""Exercise 1: Default Parameter Value
1- Create a Python function named print_message that takes a parameter message and a parameter repeat_count, where repeat_count has a default value of 1.
2- The function should print the message the number of times specified by repeat_count.
3- Prompt the user to enter a message and a repeat count (optional).
4- Call the print_message function with the user-provided values or using the default value."""

def print_message(message, repeat_count=1):
    x = 1
    while x<=repeat_count:
        print(message)
        x +=1
print_message("hello cassmates",10)





# onother Example
def print_massage(message, repeat_count=1):
    for i in range(repeat_count):
        
        print(message)

message = input("Enter a massage: ")

repeat_count = int(input("Enter a repeat count (optional):"))

print_massage(message, repeat_count)
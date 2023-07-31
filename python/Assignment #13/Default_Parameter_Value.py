# Default Parameter Value
"""The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:"""


def print_massage(message, repeat_count=1):
    for i in range(repeat_count):
        
        print(message)

message = input("Enter a massage: ")

repeat_count = int(input("Enter a repeat count (optional):"))

print_massage(message, repeat_count)
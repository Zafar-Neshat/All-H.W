# 1- creat a function named is_even that take an integer as a parameter anad returns True if number is ecen, othewise False.
# 2- Demonstrate the usage of this function by checking whether the nuber 22 is even or odd.


def is_even(num):

    if num % 2 == 0:
        return True
    else:
        return False


if is_even(22):
    print("22 is even")
else:
    print("22 is odd")

    

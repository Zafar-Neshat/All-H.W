def factorial(n):   
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
  
print(factorial(5))


# Example-2
def factorial(b):
    if b <=1:
        return 1
    else:
        return b * factorial(b-1)
print(factorial(5))
# 5 * 4 * 3 * 2 * 1 = 5



def print_triangle(n):
  for i in range(1, n + 1):
    for j in range(1, i + 1):
        
      print("*", end="")
    print()

print_triangle(5)



# Example-2
def triangle(n):
    x = 0
    while x <= n:
        print("#" * x)
        x += 1
triangle(8)
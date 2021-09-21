print("\nQ1a\n")
# Q1a: Replicate the following functions as lambda functions

# def square(n):
#     return n*n
square = lambda n: n**2


# def percentage(n):
#     return n/100
percentage = lambda n: n/100


# def multiplier(n, m):
#     return n*m
multiplier = lambda n, m: n*m


# def addition(a, b, c):
#     return a + b + c
addition = lambda a, b, c: a + b + c

# A1a:


print("\nQ1b\n")
# Q1b: Write an explanation of how this factorial lambda function works
factorial = lambda a: a*factorial(a-1) if (a>1) else 1
"""It multiplies an ideally natural number by every number smaller than it but greater than 0"""


# A1b:


print("\nQ1c\n")
# Q1c: Using the Map function alongside a lambda function, take the list_of_numbers
# and generate a list of all of the numbers squared
list_of_numbers = [23, 345, 45, 76, 87, 4, 2, 0]

print(list(map(square(), list_of_numbers)))


# A1c:


# -------------------------------------------------------------------------------------- #

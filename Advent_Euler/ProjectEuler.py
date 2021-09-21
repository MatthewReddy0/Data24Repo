import random as r

"""
# 1
x = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        x = x + i
print(f'The sum of all numbers in the range 1-1000 that are evenly divisible by 3 or 5 is {x}')

# 2
x = 0
temp = 0
y = 1
summation = 0
while y < 4000000:
    if y % 2 == 0:
        summation = summation + y
    temp = y
    y = x + y
    x = temp
print(f'The sum of all even Fibonacci numbers less than 4 million is {summation}')

# 3
i = 1
largest = 0
x = 600851475143
while i <= 600851475143:
    count = 0
    if 600851475143 % i == 0:
        j = 1
        while j <= i:
            if i % j == 0:
                count = count + 1
            j = j + 1
        if count == 2:
            largest = i
            x = x / largest
            if x == 1:
                break
    i += 1
print(f"The largest factor of 600851475143 is {largest}")

# 4
x = 0
largest = 0


def is_palindrome(x):
    if x[0:3] == x[-1:2:-1]:
        return True
    else:
        return False


for i in range(100, 999):
    for j in range(100, 999):
        x = str(i*j)
        if len(x) == 6:
            if is_palindrome(x) is True:
                largest = x
            else:
                continue
        else:
            continue
print(f'The largest palindrome that\'s a product of two 3-digit numbers is {largest}')

# 5
for i in range(19*17*13*11, 10 ^ 10, 19*17*13*11):
    if i % 20 == 0 and i % 18 == 0 and i % 16 == 0 and i % 15 == 0 and i % 14 == 0 and i % 12 == 0:
        x = i
        break
print(f'The smallest number evenly divisible by the numbers 1-20 is {x}')

# 6
summation = 0
x = 0
for i in range(100):
    summation += i
    x += i ** 2
print(f'The difference between the sum of the squares and the square of the sum of the first 100 natural numbers is'
      f' {(summation ** 2) - x}')
"""

# 17 Answer is 21124
def getno(digit):
    total = 0
    if digit in three_letter: total += 3
    elif digit in four_letter: total += 4
    elif digit in five_letter: total += 5
    elif digit in six_letter:  total += 6
    elif digit in seven_letter: total += 7
    elif digit in eight_letter: total += 8
    elif digit in nine_letter: total += 9
    return total


three_letter = [1, 2, 6, 10]
four_letter  = [4, 5, 9]
five_letter  = [3, 7, 8]
six_letter   = [11, 12]
seven_letter = [15, 16]
eight_letter = [13, 14, 18, 19]
nine_letter  = [17]

twentylets ={0:0, 2:6, 3:6, 4:6, 5:5, 6:5, 7:7, 8:6, 9:6}

total = 0
Target = 1000
for numb in range(1, Target+1, 1):
    numb = str(numb)
    length = len(numb)

    if length == 4:
        total += getno(int(numb[0]))            #for thousands's digit
        total += 8
        print(total)
        if int(numb[1]) + int(numb[2]) + int(numb[3]) == 0:
            numb = []
            length = len(numb)
        else:
            numb = numb[1::]
            length = len(numb)                      #new length
    if length == 3:
        total += getno(int(numb[0]))            #for hundred's digit
        total += 7                              #for hundred
        if int(numb[1]) + int(numb[2]) != 0:
            total += 3                          #for and
        numb = numb[1::]
        length = len(numb)                      #new length
    if length == 2 and int(numb[0]) != 1:
        total += twentylets[int(numb[0])]
        numb = numb[1::]
        length = len(numb)


    elif length == 2 and int(numb[0]) == 1:
        total += getno(int(numb[0] + numb[1]))
        numb = numb[2::]
        length = len(numb)

    if length == 1:
        total += getno(int(numb[0]))
        numb = []
        length = len(numb)

print(f"last total: {total}")

# 43

# Start with a pandigital 0-9 number
x = '0123456789'
x = list(x)
r.shuffle(x)
x = ''.join(x)
print(x)
# List of number 0123456789
# Take out 123 digits, don't keep them in
# Check even-ness
# Start with a 3-digit number, say 406
# Check even-ness
# Generate 06x, and check whether 06x is divisible by 3
# Make a list of the sub-string numbers
# Check divisibility property

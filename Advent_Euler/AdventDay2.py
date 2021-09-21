# i = '9-10 m: mmmmnxmmmwm'
#
# minimum = int(i.split('-')[0])
# maximum = i.split(' ')[0]
# maximum = int(maximum.split('-')[1])
# stringy = i.split(':')[1]
# letter = i.split(':')[0]
# letter = letter.split(' ')[1]
#
# print(minimum)
# print(stringy)
# print(maximum)
# print(letter)
#
# print(stringy.count(letter))
#
number_of_correct_passwords = 0
number_of_actually_correct_passwords = 0

with open('Advent2input.txt') as file:

    data = file.readlines()

    for i in data:
        empty_string = ''

        minimum = int(i.split('-')[0])
        maximum = i.split(' ')[0]
        maximum = int(maximum.split('-')[1])
        stringy = i.split(':')[1]
        letter = i.split(':')[0]
        letter = letter.split(' ')[1]

        empty_string += stringy[minimum]
        empty_string += stringy[maximum]

        if empty_string.count(letter) == 1:
            number_of_actually_correct_passwords += 1

        if stringy.count(letter) in range(minimum, maximum+1):
            number_of_correct_passwords += 1

    print(number_of_correct_passwords)
    print(number_of_actually_correct_passwords)

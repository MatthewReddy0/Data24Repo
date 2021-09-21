full_list = []
numbers_that_add = []

with open('Advent1input.txt') as file:

    data = file.readlines()

    for i in data:
        full_list.append(int(i))

    for i in full_list:
        for j in full_list:
            if (2020 - i - j) in full_list:
                print(i, j, 2020-i-j)

    # print(numbers_that_add[0]*numbers_that_add[1])



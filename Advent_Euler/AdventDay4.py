# Count the number of valid passports
# Passport is valid if it contains all fields
#   cid field is optional
# byr, iyr, eyr, hgt, hcl, ecl, pid, cid
# Data is stored as key-value pairs

test_list = ['iyr:2021', 'hcl:6708a3', 'ecl:zzz eyr:2034 byr:2010', 'hgt:189cm', 'pid:466438311']
test_list[0 : len(test_list)] = [''.join(test_list[0 : len(test_list)])]
print(str(test_list))

vowels = ['a', 'e', '\n\n', 'o', 'i', 'u']
index = vowels.index('e')
print('The index of e:', index)
index = vowels.index('\n\n')
print('The index of i:', index)

# \n\n is distiguishing character
# forest_map = [line.strip() for line in data]
with open('Advent4input.txt') as file:
    data = file.readlines()

    print(data[2])
    print(data.index('\n'))

    count = 0
    for indx, val in enumerate(data):
        print(indx, val)
        data[0: data.index('\n')] = [''.join(data[0: data.index('\n')])]

        count += 1
        if count > 20:
            break
        # test_list = []
        # data.index('\n\n')
        continue

print('end')


"""
ints = [8, 23, 45, 12, 78]
for i in ints:
    print('item #{} = {}'.format(???, i))

for idx, val in enumerate(ints):
    print(idx, val)
"""
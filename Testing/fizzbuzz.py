def fizz(x):
    if x % 3 == 0:
        return 'Fizz'
    else:
        return ''


def buzz(x):
    if x % 5 == 0:
        return 'Buzz'
    else:
        return ''


for i in range(100):
    stringy = ''
    stringy += fizz(i)
    stringy += buzz(i)
    if stringy == '':
        print(i)
    else:
        print(stringy)

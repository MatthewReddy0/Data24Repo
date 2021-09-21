from fizzbuzz import fizz, buzz


def test_fizz():
    assert fizz(6) == 'Fizz'
    assert fizz(100) == ''


def test_buzz():
    assert buzz(100) == 'Buzz'
    assert buzz(3) == ''

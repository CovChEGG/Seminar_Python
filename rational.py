from fractions import Fraction


def calc(a, b, action):
    a = str_frac(a)
    b = str_frac(b)
    res = Fraction(1, 1)
    if action == '+':
        res = a + b
    elif action == '-':
        res = a - b
    elif action == '*':
        res = a * b
    elif b == 0:
        print('Деление на 0 не допустимо!!!')
        exit(1)
    else:
        if action == '/':
            res = a / b
        elif action == '%':
            res = a % b
        elif action == '//':
            res = a // b
    return whole_numbers(res)


def str_frac(str1):
    str1 = str1.replace('/', ' ')
    lst1 = str1.split()
    if len(lst1) == 3:
        lst1[0] = int(lst1[0]) * int(lst1[2]) + int(lst1[1])
        lst1[2] = int(lst1[2])
        lst1.pop(1)
    elif len(lst1) == 2:
        lst1 = list(map(int, lst1))
    res = Fraction(lst1[0], lst1[1])
    return res


def whole_numbers(x):
    out = ''
    tmp = int(x.numerator/x.denominator)
    x = Fraction(x.numerator%x.denominator, x.denominator)
    return f'{tmp} {x}'

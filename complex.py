def count(x, y, action):
    a = x.replace('j', '')
    a = a.split()
    a = complex(int(a[0]), int(a[2]))
    # print(a)
    b = y.replace('j', '')
    b = b.split()
    b = complex(int(b[0]), int(b[2]))
    # print(b)
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '*':
        return a * b
    elif action == '/':
        return a / b
    else:
        print('Input error')


# print(count('5 + 10j', '5 + 10j', '/'))

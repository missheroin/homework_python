import random
import string


def generate_string(num):
    a = list(string.ascii_letters)
    stroka = ''
    for i in range(num):
        stroka += random.choice(a)
    return stroka


def comparison(stroka):
    a = list(stroka)
    count_upper = 0
    count_lower = 0
    for i in a:
        if i in string.ascii_lowercase:
            count_lower += 1
        elif i in string.ascii_uppercase:
            count_upper += 1
    if count_upper > count_lower:
        return 1
    elif count_lower > count_upper:
        return 0
    else:
        return -1


def create_list(lenght, num):
    return [generate_string(lenght) for i in range(num)]


def percentage(stroki):
    a = stroki
    upper = []
    lower = []
    middle = []
    for i in a:
        b = list(i)
        count_upper = 0
        count_lower = 0
        for j in b:
            if j in string.ascii_lowercase:
                count_lower += 1
            elif j in string.ascii_uppercase:
                count_upper += 1
        if count_upper > count_lower:
            upper.append(i)
        elif count_lower > count_upper:
            lower.append(i)
        else:
            middle.append(i)
    print('Upper letters percentage is: ', (len(upper) / len(a)) * 100, '%')
    print('Lower letters percentage is: ', (len(lower) / len(a)) * 100, '%')
    print('Equal percentage is: ', (len(middle) / len(a)) * 100, '%')


a = generate_string(10)
print(a)
print(comparison(a))
b = create_list(20, 8)
print(b)
percentage(b)

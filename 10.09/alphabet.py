import string


def alphabet_1():
    alph = []
    for i in string.ascii_lowercase:
        alph.append(i)
    return alph


def alphabet_2():
    return [i for i in string.ascii_lowercase]


def alphabet_3():
    return list(string.ascii_lowercase)


def elements_1(els):
    for i in els:
        print(i)


def elements_2(els):
    i = 0
    while i < len(els):
        print(els[i])
        i += 1



print(alphabet_1())
print(alphabet_2())
print(alphabet_3())
elements_1(alphabet_1())
elements_2(['а', 'б', 'в', 'г', 'д'])


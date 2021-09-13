# написать 2 функции сортировки по возрастанию случайного списка rand<int>[]
# 1 функция -> что угодно, можно в одну строку решить OK
# 2 функция -> стандартные функции запрещены OK (метод "пузырька")

def sortirovka_1(spisok):
    a = spisok
    a.sort()
    return a


def sortirovka_2(spisok):
    a = spisok
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


print(sortirovka_1([34, 456, 234, 14, 56, 467]))
print(sortirovka_2([45, 56, 78, 2134, 56, 68, 111]))

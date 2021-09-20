import string

set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {5, 6, 7, 8, 9, 0}
set_11 = [1, 2, 3, 4, 5, 6]
set_22 = [5, 6, 7, 8, 9, 0]
def count_letter_1(text):
    a = text
    letters = {}
    for i in string.ascii_letters:
        letters[i] = a.count(i)
    return letters


def count_letter_2(text):
    a = text
    letters = {}
    for i in a:
        letters[i] = a.count(i)
    return letters


def cities_dicti(pep, size):
    cities = {}
    cities[pep] = size
    return cities


def area_dicti(names, znach):
    n = names
    z = znach
    area = {}
    for i, j in zip(n, z):
        area[i] = j
    return area

def sets(set1, set2):
    print(set1.isdisjoint(set2))
    print(set1 == set2)
    print(set1.issubset(set2))
    print(set1.issuperset(set2))
    print(set1.union(set2))
    print(set1.intersection(set2))
    print(set1.difference(set2))
    print(set1.symmetric_difference(set2))
    print(set1.copy())
    print(set2.copy())

def unique(spis):
    return list(set(spis))

def intersec(set1, set2):
    return list(set(set1).intersection(set(set2)))

print(count_letter_1('hello'))
print(count_letter_2('helloaa'))
print(cities_dicti(1, 8))
print(area_dicti(['лондон', 'москва', 'нью-йорк'], [{'a': 1}, {'b': 2}, {'c': 3}]))
sets(set_1, set_2)
print(intersec(set_11, set_22))
print(unique(set_1))



#1) функция unique
#    list -> list
#находит все уникальные значения в списке
#2) функция intersection
#    list, list -> list
#находит все пересекающиеся элементы в 2х списках
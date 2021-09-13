def palindrom(stroka):
    if stroka == stroka[::-1]:
        return True
    else:
        return False


def extension(file):
    a = file
    if '.' in a:
        a = file.split('.')
        return a[-1]
    else:
        return 'Invalid sintax'


def sec_to_time(seconds):
    sec = seconds
    time = ['00', '00', '00', '00']
    if sec // 86400:
        time[0] = str(sec // 86400)
        sec -= 86400 * (sec // 86400)
    if sec // 3600:
        time[1] = str(sec // 3600)
        sec -= (3600 * (sec // 3600))
    if sec // 60:
        time[2] = str(sec // 60)
        sec -= (60 * (sec // 60))
        time[-1] = str(sec)
    return time[0] + ':' + time[1] + ':' + time[2] + ':' + time[-1]


def lotsoff(chislo):
    n = str(chislo)
    a = n + ' + ' + n * 2 + ' + ' + n * 3 + ' = '
    b = int(n) + int(n * 2) + int(n * 3)
    return a, b


print(palindrom('заказ'))
print(extension('filetxt'))
print(lotsoff(2))
print(sec_to_time(86400))

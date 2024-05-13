def task1():

    s = 'YYYYggkeeeAAABV'

    counter = 1
    a = ''

    for i in range(0, len(s)-1):
        if s[i+1] == s[i]:
            counter += 1
        else:
            if counter != 1:
                a += str(s[i]) + str(counter)
            else:
                a+= str(s[i])
            counter = 1

    print(a)


def task2():
    s = 'Y4g2ke3A3BV'
    a = ''
    counter = 1
    i = 0

    while i < (len(s)):
        if i == (len(s)-1) and ((s[i] >= 'a') and (s[i] <= 'z') or (s[i] >= 'A') and (s[i] <= 'Z')):
            a += s[i]
            break
        if ((s[i] >= 'a') and (s[i] <= 'z') or (s[i] >= 'A') and (s[i] <= 'Z')):
            if ((s[i+1] >= 'a') and (s[i+1] <= 'z') or (s[i+1] >= 'A') and (s[i+1] <= 'Z')):
                a += s[i]
                i += 1
            else:
                j = i+1
                while not((s[j] >= 'a') and (s[j] <= 'z') or (s[j] >= 'A') and (s[j] <= 'Z')):
                    j += 1

                counter = int(s[i+1:j])
                a += s[i] * counter
                i = j
        else:
            i+=1

    print (a)


def task3():
    a1 = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    a2 = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    a3 = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    u = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    n = int(input())

    if n == 1000:
        print('тысяча')
        return

    if n>=1 and n<=9:
        print(a1[n])
        return

    if n>=10 and n<= 19:
        print(a2[n%10])
        return

    if n>=20 and n<=99:
        print(a3[(n//10)-1], a1[n%10])
        return

    if n>=100 and n<=999:
        if (n%100)//10 == 1:
            print(u[n//100-1], a2[n%10])
        elif (n%100)//10 == 0:
            print(u[n // 100 - 1], a1[n % 10])
        else:
            print(u[n//100-1], a3[((n%100)//10)-1], a1[n%10])
        return

def task4():
    d = {}

    s = ''
    s = input()
    i = 0
    start = -1

    while i < len(s):
        if s[i] == "'" and start == -1:
            start = i
        elif s[i] == "'" and start != -1:
            if d.get(s[start+1:i]) == None : #уникальная строка
                d[s[start+1:i]] = 1
            else:
                d[s[start + 1:i]] += 1
            start = -1
        i += 1
    l = ''
    for i in d.keys():
        l += str(d[i]) + ' '

    print(l)

def task5():
    mat = []

    for i in range(3):
        mat.append([0]*3)
        for j in range(3):
            mat[i][j] = int(input())

    flag = 1

    for i in range(2):
        for j in range(i+1, 3):
            k = mat[i][0]/mat[j][0]
            for n in range(3):
                if mat[i][n]/mat[j][n] != k:
                    flag = 0
            if flag == 1:
                print('yes')
                return

    print('no')
    return

def task6():
    s = ''
    s = input()
    res = ''
    i = 1

    if s[0] >= 'а' and s[0] <= 'я':
        res = s[0]

    while i < len(s):
        if (s[i] >= 'а' and s[i] <= 'я' or s[i] >= 'А' and s[i] <= 'Я') and not(s[i-1] >= 'а' and s[i-1] <= 'я' or s[i-1] >= 'А' and s[i-1] <= 'Я'):
            res += s[i]
        i += 1

    print(res.upper())

task6()
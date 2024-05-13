def task1():
    d = {}
    s = input()

    i = s.find(',')
    d[int(s[0:i])] = 0
    i += 1

    while i < len(s):
        tmp = s.find(',', i, len(s))
        if tmp == -1:
            tmp = len(s)-1
        d[int(s[i+1:tmp])] = 0
        i = tmp+1

    print(len(d))

def task2():
    d = {}
    d1 = {}
    s = input()
    s1 = input()

    i = s.find(',')
    d[int(s[1:i])] = 0
    i += 1
    while i < len(s):
        tmp = s.find(',', i, len(s))
        if tmp == -1:
            tmp = len(s) - 1
        d[int(s[i + 1:tmp])] = 0
        i = tmp + 1

    i1 = s1.find(',')
    d1[int(s1[1:i1])] = 0
    i1 += 1
    while i1 < len(s1):
        tmp1 = s1.find(',', i1, len(s1))
        if tmp1 == -1:
            tmp1 = len(s1) - 1
        d1[int(s1[i1 + 1:tmp1])] = 0
        i1 = tmp1 + 1

    for n in d.keys():
        if d1.get(n) == None:
            print('False')
            return

    if len(d) == len(d1) :
        print('False')
    else:
        print('True')

def task3():
    n = int(input())
    d = {}

    while len(d) < n:
        word = input().lower()
        if d.get(word) == None:
            d[word] = 0
            print('OK')
        else:
            print('REPEAT')

def task4():
    d = {}
    s = input()

    d[s[0:s.find(' ')]] = 0

    i = s.find(' ')+1
    print ('0 ')

    while i < len(s):
        if i != ' ':
            if s.find(' ', i, len(s)) == -1:
                key = s[i:len(s)]
            else:
                key = s[i:s.find(' ', i, len(s))]

            if d.get(key) == None:
                d[key] = 0
            else:
                d[key] += 1
            print(d[key], ' ')

            if s.find(' ', i, len(s)) == -1:
                i = len(s) + 1
            else :
                i = s.find(' ', i, len(s)) + 1

def task5():
    n = int(input())

    strings = []

    for i in range(n):
        strings.append(input())

    d = {}
    min_id = 1000000
    max_id = 0

    for i in range(n):
        id = int(strings[i][0:strings[i].find(' ')])
        t = strings[i][strings[i].find(' ') + 1:strings[i].rfind(' ')]
        k = int(strings[i][strings[i].rfind(' ')+1:])

        min_id = min(min_id, id)
        max_id = max(max_id, id)
        if d.get((id, t)) == None:
            d.update({(id, t): k})
        else:
            d[(id, t)] = d[(id,t)] + k

    for i in range(min_id, max_id+1):
        for j in d.keys():
            if i == j[0]:
                print(j[0], j[1], d[j])


def task6():

    s = input()
    d = {}
    start = 0
    finish = 0

    while start < len(s) :
        finish = s.find(' ', start, len(s))
        if finish == -1:
            break
        word = s[start:finish]
        start = finish + 1
        if d.get(word) == None :
            d[word] = 1
        else:
            d[word] += 1

    for i in d.keys():
        print(i, d[i])

task6()
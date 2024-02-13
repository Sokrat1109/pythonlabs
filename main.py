def task1():
    a = int(input())
    b = int(input())
    c = int(input())

    if a == b and a == c and b == c:
        print(3)
    elif a != b and a != c and b != c:
        print(0)
    else:
        print(2)

def task2():
    n = int(input())
    l = ''
    for i in range(1, n+1):
        l += str(i)
        print(l)


def task3():
    m = int(input())
    s = ''
    k = ''
    for i in range(1, m+1):
        if i == 1:
            k = '1'
        else:
            k = str(i)+k+str(i)
        s = ' '*(m-i)+k+' '*(m-i)
        print(s)

def task4():
    n = int(input())
    counter = 0
    for i in range(2, n+1):
        while i != 0:
            counter += 1
            i //=10
    l = ''
    s = ''
    ll = ''
    for i in range(1, n + 1):
        if i == 1:
            s = '1'
        else:
            s = str(i) + s + str(i)
        l = ' ' * counter + s + ' ' * counter
        h = 0
        while i != 0:
            h += 1
            i //=10
        counter = counter - h

        print(l)

#task1()
#task2()
#task3()
task4()
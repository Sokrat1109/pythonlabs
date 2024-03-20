def Fact(a):
    if a <= 1:
        return 1
    else:
        return a*Fact(a-1) # рекурсия

n = int(input())
s = ['']*(n+1)

for i in range(0, n+1):
    for j in range(0, i+1):
        s[i] += str(int(Fact(i)/(Fact(j)*Fact(i-j)))) + ' '
    s[i] = s[i][:-1:]

counter = len(s[n])

for i in range(0, n + 1):
    c = (counter-len(s[i]))//2
    l = ' ' * c + s[i] + ' ' * c
    print(l)
def Fact(a):
    if a <= 1:
        return 1
    else:
        return a*Fact(a-1) # рекурсия


n = int(input())
n = 2**(1+n)
s = ['']*(n+1)

for i in range(0, n+1):
    for j in range(0, i+1):
        c_k_n = int(Fact(i)/(Fact(j)*Fact(i-j)))
        if c_k_n % 2 == 1:
            c_k_n = '*'
        else:
            c_k_n = ' '
        s[i] += c_k_n + ' '
    s[i] = s[i][:-1:]


counter = len(s[n])

for i in range(0, n ):
    c = (counter-len(s[i]))//2
    l = ' ' * c + s[i] + ' ' * c
    print(l)

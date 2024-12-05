import random
a, a1 = [], []
b, b1 = [], []
n = 6
m = 20
for i in range(n):
    for j in range(m):
        a.append(random.randint(0,9))
        a1.append(" ")
    b.append(a)
    b1.append(a1)
    print(a)
    a, a1 = [], []
m1 = 1
k = -1
l = -1
p = 1
n += l
while m1 < m-1:
    for i in range(n, k, l):
        b1[i][m1] = b[i][m1]
        p = i
    m1 += 1
    b1[p][m1]=b[p][m1]
    l *= -1
    m1 += 1
    n += l
    k += l
    p = n
    n = k
    k = p

for i in range(p):
    for j in range(m):
        if b1[i][j] != " ":
            print(b1[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()
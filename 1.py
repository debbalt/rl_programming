a = list(range(2,11))
answer = []
b = a[:]
c = 0
for i in range(len(a)):
    k = []
    for j in range(len(b)):
        k.append(a[i]+b[j])
    answer.append(k)
for i in answer:
    print(*i)

def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return y


n = int(input())
p = []
for i in range(n):
    p.append(input())

P = 0
Q = 1
for i in p:
    Q *= int(i.split('/')[-1])

for i in p:
    P += int(i.split('/')[0]) * (Q / int(i.split('/')[-1]))

P = int(P)
Q = int(Q)

if P % Q == 0:
    print(int(P / Q))
else:
    gcdr = gcd(P, Q)
    print(f'{int(P / gcdr)}/{int(Q / gcdr)}')

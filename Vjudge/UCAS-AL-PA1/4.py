"""
现在有 nn 个分数并想对他们求和，并用最简形式来表示。所谓最简形式是指：分子分母的最大公约数为 1；若最终结果的分母为 1，则直接用整数表示。

如：5/6、10/3 均是最简形式，而 3/6 需要化简为 1/2, 3/1 需要化简为 33。

分子和分母均不为 0，也不为负数。

输入格式
第一行是一个整数 n，表示分数个数，1≤n≤10；

接下来 nn 行，每行一个分数，用 "p/q" 的形式表示，不含空格，p，q 均不超过 10。

输出格式
输出只有一行，即最终结果的最简形式。若为分数，用 "p/q" 的形式表示。
"""


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

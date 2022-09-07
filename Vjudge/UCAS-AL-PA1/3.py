"""
求两个不超过200位的非负整数的和。

输入格式
有两行，每行是一个不超过200位的非负整数，可能有多余的前导 00。

输出格式
一行，即相加后的结果。结果里不能有多余的前导 00，即如果结果是 342，那么就不能输出为 0342。

输入输出样例"""

i1 = input()
i2 = input()

if len(i1) < len(i2):
    n1 = i1
    n2 = i2
else:
    n1 = i2
    n2 = i1

n1 = n1[::-1]
n2 = n2[::-1]

# len n1  < len n2
result = []
c = 0
for i in range(len(n1)):
    result.append((int(n1[i]) + int(n2[i]) + c) % 10)
    c = (int(n1[i]) + int(n2[i]) + c) // 10
for i in range(len(n1), len(n2)):
    result.append((int(n2[i]) + c) % 10)
    c = (int(n2[i]) + c) // 10
result.append(c)
flag = len(result)

for i in range(len(result)):
    if result[-1 - i] != 0:
        flag = i
        break
result = result[::-1][flag:]
r = ''
for i in range(len(result)):
    r += str(result[i])

print(r if r != '' else '0')

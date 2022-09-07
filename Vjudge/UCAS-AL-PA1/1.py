strIn = input()
strIn = strIn.replace(',', ' ')
list = strIn.split()

lmax = -1
lmin = 0x8FFFFFFF
strmax = ''
strmin = ''
if len(list) != 0:
    for i in list:
        if len(i) > lmax:
            strmax = i
            lmax = len(i)
        if len(i) < lmin:
            strmin = i
            lmin = len(i)
print(strmax)
print(strmin)

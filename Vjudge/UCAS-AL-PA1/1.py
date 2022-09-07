"""
输入1行句子，该句子只包含字母和空格。单词由至少一个连续的字母构成，空格和逗号都是单词间的间隔。

试输出第1个最长的单词和第1个最短单词。

输入格式
一行句子。

输出格式
两行输出：

第1行，第一个最长的单词。

第2行，第一个最短的单词。

提示
如果所有单词长度相同，那么第一个单词既是最长单词也是最短单词。
"""

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

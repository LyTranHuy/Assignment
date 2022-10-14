#Bai 1

"""string = str(input())
nstr = list(string)
nstr[5] = 'k'
for i in nstr:
    print (i, end ='')
"""

#Bai 2
"""from ast import Break
from xmlrpc.client import boolean


nums = [2, 7, 11, 15]
target = 9
flag = False
for i in range (0, len(nums)-1):
    temp = target - nums[i]
    if temp > 0:
        for j in range (0, len(nums)-1):
            if nums[j] == temp:
                print (i, j)
                flag = True
    if flag:
        break"""

#Bai 3

"""n_str = int(input())
wordlist = list()
count ={}
for i in range(n_str):
    word = input()
    wordlist.append(word)
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(len(count))
result ={}
for i in count:
    y = count.get(i)
    print(y, end = ' ')"""

#Bai 4
def CheckFirstNum(s):
    nstr = list(str(s))
    first = int(nstr[0])
    if first in range (4, 6):
        return True
    else:
        return False
def CheckNumber(s):
    nstr = list(str(s))
    number = str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    dem = 0
    for i in nstr:
        if i =='-':
            continue
        if i not in number:
            dem += 1
    if dem >= 1:
        return False
    else:
        return True 
def CheckRepeated(s):
    n = len(s)
    ch = s[0]
    count = 1
    for i in range(1, n):
        if s[i] == '-':
            continue
        if s[i] == ch:
            count += 1
            if count == 4:
                return False
        else:
            ch = s[i]
            count = 1
    return True 
def CheckHyphen(s):
    if s.count('-') == 0 or s.count('-') == 3:
        return True
    else:
        return False

s = input()
x = len(s)
if x == 16 or x == 19:
    if CheckFirstNum(s) and CheckHyphen(s) and CheckNumber(s) and CheckRepeated(s):
        print ("Valid")
    else:
        print("Invalid")


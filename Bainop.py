#Bai 1

"""string = str(input())
nstr = list(string)
nstr[5] = 'k'
for i in nstr:
    print (i, end ='')
"""

#Bai 2
from ast import Break
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
        break
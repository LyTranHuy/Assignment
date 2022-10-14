#Bai 1 
"""
string = 'abracadabra'
nstr = list(string)
nstr[5] = 'k'
string = ''.join(nstr)
print (string)
"""
"""
#bai 2
def twoSum(nums: list[int], target: int):
    result = []
    index_map = {}
    for i, n in enumerate(nums):
        difference = target - n
        if difference in index_map:
            result.append(i)
            result.append(index_map[difference])
            break
        else:
            index_map[n] = i
    return result
Mang = list([2, 7, 11, 15])
Target = 9
print(twoSum(Mang, Target))
"""
"""#Bai 3
from collections import Counter
n_str = int(input())
l = list()
for i in range(n_str):
    l.append(input())
x = Counter(l)
print(len(x))
for i in x.values():
    print(i, end=" ")
"""
#Bai 4
import re
n = int(input())
for t in range(n):
    credit = input().strip()
    credit_removed_hiphen = credit.replace('-','')
    valid = True
    length_16 = bool(re.match(r'^[4-6]\d{15}$',credit))
    length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$',credit))    
    consecutive = bool(re.findall(r'(?=(\d)\1\1\1)',credit_removed_hiphen))
    if length_16 == True or length_19 == True:
        if consecutive == True:
            valid=False
    else:
        valid = False       
    if valid == True:
        print('Valid')
    else:
        print('Invalid')
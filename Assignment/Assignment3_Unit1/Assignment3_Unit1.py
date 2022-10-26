
# Make tool to check if the first number wrong
def CheckFirstNum(s):
    nstr = list(str(s))
    first = int(nstr[0])
    if first in range (4, 6):
        return True
    else:
        return False
# Make tool to check if the list number content other characters
def CheckNumber(s):
    nstr = list(str(s))
    number = str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    count = 0
    for i in nstr:
        if i =='-':
            continue
        if i not in number:
            count += 1
    if count >= 1:
        return False
    else:
        return True 
# Make tool to check if one number repeated more than 4 times
def CheckRepeated(s):
    n = len(s)
    temp = s[0]
    count = 1
    for i in range(1, n):
        if s[i] == '-':
            continue
        if s[i] == temp:
            count += 1
            if count == 4:
                return False
        else:
            temp = s[i]
            count = 1
    return True 
# Make tool to check if the hyphen use wrong
def CheckHyphen(s):
    if s.count('-') == 0 or s.count('-') == 3:
        return True
    else:
        return False
# Make tool to check the Credit card number that content all the tool below
def final_check(s):
    x = len(s)
    if x == 16 or x == 19:
        if CheckFirstNum(s) and CheckHyphen(s) and CheckNumber(s) and CheckRepeated(s):
            return("Valid")
        else:
            return("Invalid")
    else:
        return("Invalid")
# s = input()
# print(final_check(s))
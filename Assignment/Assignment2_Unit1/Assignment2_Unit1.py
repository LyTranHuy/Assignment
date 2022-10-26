#Assignment 2

def two_sum(n, nums, target):
    # Input number of item 
    try :                       
        index = int(n)
    # If index is not an interger
    except:                 
        return ("Data type not true")
    # If index is intergers but below 0
    if index < 0:                
        return ("Sorry, numbers below zero not alowwed")
    new_nums = [] 
    # Input item of array
    for i in range (index):
        try :                       
            num = int(nums[i])
        except:                 
            return("Data type not true")
        new_nums.append(num)
    try: 
        truetarget = int(target)
    except:
        return ("Type not true")
    # Set flag for out the loop
    flag = False
    for i in range (0, index):
        temp = truetarget - nums[i]
        for j in range (0, len(nums)):
            if nums[j] == temp:
                flag = True 
                return (i, j)
        if flag:
            break
    if flag == False:
        return("None item")
# n = input()
# nums = []
# target = input()
# print(return_index(n, nums, target))

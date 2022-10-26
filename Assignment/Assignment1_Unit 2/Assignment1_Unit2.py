
def replace_char(string, x, char):
    nstr = list(string)         # Turn string to array
    try :                       # If index is not an interger
        index = int(x)
    except:                 
        return ("Data type not true")
    if index < 0:               # If index is intergers but below 0 
        return ("Sorry, no numbers below zero")
    elif index > (len(nstr)):   # If index more than length of string input
        return ("Index is more than the length of string")
    nstr[index] = char          # Replace char at index
    result = ''
    for i in nstr:
        result = result + i
    return(result)
          
"""string = input()       
x = input()            
char = input()         
print(replace_char(string, x, char))"""


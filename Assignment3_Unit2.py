import os
path = 'D:\\TestCode\\Assignment\\Assignment3_Unit2\\find_the_flag'
data = []
for root, dirs, files in os.walk("D:\\TestCode\\Assignment\\Assignment3_Unit2\\find_the_flag"): 
    for file in files:
        path = os.path.join(root, file)
        with open(path) as inf:
            data.append(inf.read())

def find_file(char):
    if char == "Not a flag":
        for x in data:
            if "Not" in x:
                return(x)
    else:             
        for x in data:
            if char in x:
                return(x)
            
char = input()
print(find_file(char))
         
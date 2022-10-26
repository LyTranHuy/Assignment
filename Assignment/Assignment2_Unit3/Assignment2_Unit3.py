

def not_duplicated(n, wordlist):
    try:
        n_str = int(n)
    except:
        return ("Data type not true")
    if n_str < 0:
        return ("Negative not allowwed")
    count = {}
    # Call loop to fill ditionary count
    for i in wordlist:
        if i in count:
            count[i]+=1 # If string appeared more than 1 => key +1
        else:
            count[i]=1 # If string just appeared one time => key = 1
    result = []
    for i in count:
        y = count.get(i)
        result.append(y)
    return(len(count), result)  # Return how much string that appeared and how many time that a string duplicated
# n = input()
# wordlist = []
# print(not_duplicated(n, word))

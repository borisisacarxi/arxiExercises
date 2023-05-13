a = ['ola', 'pai', 'Aaron']

def listToDict(arr=[]):
    b={}
    count=1
    for word in arr:
        b[word] = count
        #print(b)
        count+=1
    return b

print(listToDict(a))
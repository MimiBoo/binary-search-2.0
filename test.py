from math import floor


testList = ['12A','13A','15A','14B', '16C']#data list
testList.sort()#sort the data list

def translateToAscii(Tlist):
    tempItem = ""
    tempList = []
    for i in Tlist:
        for j in i:
            tempItem += str(ord(j))
        tempList.append(int(tempItem))
        tempItem = ''
    return tempList
temp = translateToAscii(testList)


def search(array, length, target):
    T = ""
    for i in target:
        T += str(ord(i))
    
    L = 0
    R = length - 1
    while L <= R:
        M = floor((L+R)/2)
        if array[M] < int(T):
            L = M + 1
        elif array[M] > int(T):
            R = M - 1
        else:
            return M
    return None
temp = translateToAscii(testList)
print(search(temp,len(temp), "15A"))
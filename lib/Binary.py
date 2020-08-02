from math import floor

class Binary2:
    def __init__(self, array):
        self.list = array
        self.list.sort()
        print(f"Sorted list: {self.list}")
        self.length = len(array)
    
    def translateToAscii(self):
        tempItem = ""
        tempList = []
        for i in self.list:
            for j in i:
                tempItem += str(ord(j))
            tempList.append(int(tempItem))
            tempItem = ''
        return tempList
    

    def search(self, target):
        array = self.translateToAscii()
        T = ""
        for i in target:
            T += str(ord(i))
        L = 0
        R = self.length - 1
        while L <= R:
            M = floor((L+R)/2)
            if array[M] < int(T):
                L = M + 1
            elif array[M] > int(T):
                R = M - 1
            else:
                return M
        return f'[{target}] Doesn\'t exist in the given list'
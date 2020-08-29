from lib import Binary
testList = ['12A','13A','15A','14B', '16C']#data list

bin2 = Binary.Binary2(testList)

bin2.translateToAscii()

res = bin2.search('15C')

print(res)
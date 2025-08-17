# Tuple 1
tup1 = (4, 3, 2, 2, -1, 18)
num = 0
result = tup1[0]
len0 = len(tup1) - 1
for i in range(len0):
    num += 1
    result = result * tup1[num]
    
print(result)
# Tuple 2
tup2 = (2, 4, 8, 8, 3, 2, 9)
divide1 = tup2[0]
num = 0
len1 = (len(tup2) - 1)
for i in range(len1):
    num += 1
    divide1 = divide1 * tup2[num]
    
print(divide1)



n1 = [1, 2, 3]
n2 = [4, 5, 6]
result = map(lambda x, y: x * y, n1, n2)
print(list(result))

n3 = [1, 2, 3, 4, 5, 6, 7]
def sq(n):
    return n * n

result2 = map(sq, n3)
print(list(result2))
tuplex = [1, "string", True, 3.2]
print(tuplex)

# create a table

tuplex =(1, 3, 5, 6, 10, 11, 15)
# tuples are immututable, so you can not add new elements
# using merge of tuples with thr + operator you can add an element and it will create a new tuple

tuplex = tuplex + (9,)
print(tuplex)

# Counts the number of occurences of item 50 from a tuple
tuple1 = [10, 50, 21, 31, 41, 50, 60]
print(tuple1.count(50))

# create a tuple
tuple2 = (10, 3, 4, 6, 2, 1, 5, 100)
_slice = tuple2[3:5]
print(_slice)
# If starting index isnt defined, it starts from the beginning
_slice = tuple2[2:5]
print(_slice)
import array as arr

array_num = arr.array('i', [1, 2, 3, 4, 5])
print("Original array:" + str(array_num))

# Count number of occurences
print("Number of occurences in 3:" + str(array_num.count(3)))

# reverse the array
array_num.reverse()
print(str(array_num))
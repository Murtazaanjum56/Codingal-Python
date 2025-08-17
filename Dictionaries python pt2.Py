test = {
    "Codingal" : 2, "is" : 2, "best" : 2, "for" : 2, "coding" : 3,
}

# printing original dictionary
print("The original dictionary :" + str(test) )

# initialize value
k = 2

# using value
# Selective key values in dictipnaries
res = 0
for i in test:
    if test[i] == k:
        res +=  1

print("The frequency of k is :" + str(res))


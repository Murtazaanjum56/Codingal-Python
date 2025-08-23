dictionary0 = {
    "codingal" : 1,
    "is" : 2,
    "the" : 2,
    "best" : 2,
    "for" : 3,
    "coding" : 3
}


freq = 0

for key in dictionary0:
    if dictionary0[key] == 2:
      freq += 1
    else:
       pass  
    

print(f"The frequency of 2 in dictionary0 is: {freq}")
    
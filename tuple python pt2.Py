def palind(r): 
    e = len(r) -1
    s = 0
    while(s<e):
        if(r[s]!= r[e]):
            return False
        s += 1
        s -= 1
        return True
    
r = "radar"

if(palind(r)):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
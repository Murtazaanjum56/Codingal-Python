class A:
    def __init__(self, a):
        self.a = a
        
    
    def __lt__(self, other):
        if (self.a < other.a):
            return "obj1 is  less than obj2"
        else:
            return " obj1 is not less than obj2"

    def __eq__(self, other):
        if self.a == other.a:
            return " obj1 is equal to obj2"

obj1 = A(2)
obj2 = A(3)

print("passed value:", obj1.a, obj2.a)

print(obj1.a < obj2.a)
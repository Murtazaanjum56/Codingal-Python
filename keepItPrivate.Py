
class MyClass:
    __privateVariable = 20

    def __privateMethod(self):
        print("I am inside my class")

    def hello(self):
        print(MyClass.__privateVariable)
        self.__privateMethod()

obj = MyClass()
obj.hello()
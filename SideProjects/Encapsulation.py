#  Encapsulation assignment


class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20 # Protected
        self.__c = 30 # Private

hello = Hello('name')
print(hello.a)
print(hello._b)
print(hello.__c) # Private won't be changed

        

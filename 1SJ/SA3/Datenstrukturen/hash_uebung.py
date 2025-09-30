class Person:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

p1 = Person('Alice')
p2 = Person('Bob')

print(p1)
print(p1.__eq__(p2))
# print(hash(p1))


var1 = 1
var2 = True
var3 = 1.0


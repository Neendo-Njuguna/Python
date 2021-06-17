x = [100,110,120,130,140,150]
z= []
for  y in x:
    if "a" in y:
        z.append(y)
print(z)

def divisible_by_three(*args):
    modulus = 0
    for n in args:
        modulus %= n
        return modulus


x=[[1,2],[3,4],[5,6]]
flat_list = []
z = list(x)
print(z)


def smallest(self):
    x = [3,6,8,2,4,1,5,7]
    return min(x)


def set(self):
    x = ['a','b','a','e','d','b','c','e','f','g','h']
    z = set(x)
print(z)


students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
def greet (**kwargs):
    keys = kwargs.keys()
    if "name" in keys:
        name = kwargs["name"]
        age = kwargs["age"]
        return f"Hello{name} you were born in the year{2021}-{age}"



class Rectangle:
    def __init__(self, width,length):
        self.width = width
        self.length = length
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return self.length+self.width



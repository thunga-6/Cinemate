# Operator Overloading using + and *
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def display(self):
        print(f"Vector({self.x}, {self.y})")

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Using overloaded +
v4 = v1 * 3   # Using overloaded *
v3.display()
v4.display()


# Function Overloading using len() and pop()
class CustomList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def pop(self, index=-1):
        return self.items.pop(index)

cl = CustomList([10, 20, 30, 40])
print(len(cl))  # Overloaded len()
print(cl.pop())  # Overloaded pop() - removes last item
print(cl.pop(0))  # Removes first item

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}|{self.y}'

p = Punkt(3, 4)
print(p)

print(f"x = {p.x}, y = {p.y}")  # lesender Zugriff auf die Attribute

p.x, p.y = 7, 9  # schreibender Zugriff auf die Attribute
print(p)
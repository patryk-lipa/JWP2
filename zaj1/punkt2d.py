import math

class Punkt2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt2D({self.x}, {self.y})"

    def dlugosc(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def przesun(self, dx, dy):
        self.x += dx
        self.y += dy

    @staticmethod
    def odleglosc(punkt1, punkt2):
        return math.sqrt((punkt1.x - punkt2.x) ** 2 + (punkt1.y - punkt2.y) ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Punkt2D(self.x + other.x, self.y + other.y)

# Przykłady użycia:
punkt1 = Punkt2D(3, 4)
print(punkt1)  # Powinno wydrukować: Punkt2D(3, 4)
print(punkt1.dlugosc())  # Powinno wydrukować: 5.0

punkt1.przesun(1, -2)
print(punkt1)  # Powinno wydrukować: Punkt2D(4, 2)

punkt2 = Punkt2D(1, 1)
print(Punkt2D.odleglosc(punkt1, punkt2))  # Powinno wydrukować odległość między punkt1 a punkt2

print(punkt1 == punkt2)  # Powinno wydrukować: False
punkt2.przesun(3, 1)
print(punkt1 == punkt2)  # Powinno wydrukować: True

p3 = punkt1 + punkt2
print(p3)                # Powinno wydrukować Punkt2D(8,4) 
# test commit

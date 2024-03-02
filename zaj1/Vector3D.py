import math

class Vector3D:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self) -> str:
        return f"Vector3D({self.__x}, {self.__y}, {self.__z})"

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def z(self):
        return self.__z
    
    @z.setter
    def z(self, value):
        self.__z = value


    def norm(self):
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    def __add__(self, other):
        return Vector3D(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __sub__(self, other):
        return Vector3D(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __mul__(self, scalar):
        return Vector3D(self.__x * scalar, self.__y * scalar, self.__z * scalar)

    def dot(self, other):
        return self.__x * other.__x + self.__y * other.__y + self.__z * other.__z

    def cross(self, other):
        c_x=self.__y * other.z - self.__z * other.y 
        c_y=self.__z * other.x - self.__x * other.z
        c_z=self.__x * other.y - self.__y * other.x
        return Vector3D(c_x, c_y, c_z)

    def are_orthogonal(self, other):
        return self.dot(other) == 0

a = Vector3D(1, 2, 3)
b = Vector3D(2, 3, 4)
b.x = 3
b.y = 4
b.z = 5

if __name__ == '__main__':
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"a norm: {a.norm()}")
    print(f"a + b: {a + b}")
    print(f"a * 4: {a * 4}")
    print(f"a.dot(b): {a.dot(b)}")
    print(f"a.cross(b): {a.cross(b)}")
    print(f"a.are_orthogonal(b): {a.are_orthogonal(b)}")

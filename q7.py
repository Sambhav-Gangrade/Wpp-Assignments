import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rotation(self):
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

# Example usage
vector1 = Vector2D(1, 2)
vector2 = Vector2D(3, 4)
print("-----VECTOR 2-D-----")
print("Magnitude:", vector1.magnitude())
print("Rotation:", vector1.rotation())
print("Distance:", vector1.distance(vector2))
print("Dot Product:", vector1.dot_product(vector2))
print("Cross Product:", vector1.cross_product(vector2))

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return self.__str__()

# Example usage
vector3D1 = Vector3D(1, 2, 3)
vector3D2 = Vector3D(4, 5, 6)
print("-----VECTOR 3-D-----")
print("Magnitude:", vector3D1.magnitude())
print("Distance:", vector3D1.distance(vector3D2))
print("Dot Product:", vector3D1.dot_product(vector3D2))
print("Cross Product:", vector3D1.cross_product(vector3D2))

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_type(self):
        if self.a == self.b and self.b == self.c:
            print("Равносторонний треугольник")
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            print("Равнобедренный треугольник")
        else:
            print("Разносторонний треугольник")

triangle = Triangle(2, 3, 5)
triangle.check_type()

triangle2 = Triangle(5, 5, 5)
triangle2.check_type()
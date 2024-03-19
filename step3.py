class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num != 0:
            self.result /= num


calc = Calculator()
calc.add(5)
calc.subtract(2)
calc.multiply(3)
calc.divide(4)

print(calc.result)
class Calculator:
    
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        result = 1
        for i in range(y):
            result *= x
        return result

    def square_root(self, x):
        if x == 0 or x == 1:
            return x
        val = x
        precision = 0.1
        while abs(val - x / val) > precision:
            val = (val + x / val) / 2
        return val

    def calculate(self, operation, x, y):
        if operation == "add":
            result = self.add(x,y)

        elif operation == "subtract":
            result = self.subtract(x,y)

        elif operation == "multiply":
            result = self.multiply(x,y)

        elif operation == "divide":
            result = self.divide(x,y)

        elif operation == "power":
            result = self.power(x,y)

        elif operation == "square_root":
            result = self.square_root(x)
        return result


operation = input("Enter the operation you would like to perform (add, subtract, multiply, divide, square_root, power): ")
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the secod number : "))

# Partie de TEST
calcul = Calculator()
print(calcul.calculate(operation, num1, num2))

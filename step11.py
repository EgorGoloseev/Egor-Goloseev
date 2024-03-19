def factorial(n):
    factorial = 1
    if n < 0:
        return "Факториал определен только для целых неотрицательных чисел"
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
            factorial = i
        return factorial

print(factorial(7))
print(factorial(0))
print(factorial(10))
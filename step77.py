def exponentiation(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

print(exponentiation(2, 3))
print(exponentiation(4, 2))
print(exponentiation(3, 5))
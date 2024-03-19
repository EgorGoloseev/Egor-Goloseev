total = 0

def add_to_total(number):
    global total
    total += number

add_to_total(5)
add_to_total(10)
add_to_total(15)
print(total)
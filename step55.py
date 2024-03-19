def increment():
    if 'counter' not in locals():
        counter = 0
    else:
        counter += 1
    print(counter)

increment()
increment()
increment()
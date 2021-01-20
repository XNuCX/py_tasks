def bit_counting(number):
    number = int(number)
    result = []
    while not (number == 0):
        if number % 2 == 0:
            result.append(0)
            number /= 2
        else:
            result.append(1)
            number //= 2

    return result[-1::-1].count(1)

print(bit_counting(1111))
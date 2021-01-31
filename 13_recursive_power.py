def recursive_power(num, power, result = 1):

    if power == 0:
        return result
    result *= num
    return recursive_power(num, power-1, result)

print(recursive_power(2, 10))
print(recursive_power(10, 100))
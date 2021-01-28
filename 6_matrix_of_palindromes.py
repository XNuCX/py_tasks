r, c = [int(el) for el in input().split(" ")]
char = chr(97 + r)

matrix =print('\n'.join([' '.join([chr(97 + row) + chr(97 + col + row) + chr(97 + row)for col in range(c)]) for row in range(r)]))

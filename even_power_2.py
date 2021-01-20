n = int(input())
if n % 2 == 0:
    for i in range(0, n+1, 2):
        print(2**i)
else:
    for i in range(0, n, 2):
        print(2**i)
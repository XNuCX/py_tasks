n = int(input())

for i in range(0, n):

    for k in range(0, n):

        for m in range(0, n):
            print(f"{chr(97+i)}{chr(97+k)}{chr(97+m)}")
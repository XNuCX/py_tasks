a = float(input())
is_valid = -100 <= a <= 100 and a != 0
if is_valid:
    print("Yes")
else:
    print("No")
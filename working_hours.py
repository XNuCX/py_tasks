h = int(input())
w_d = input()
is_valid_h = 10 <= h <= 18
is_valid_w_d = w_d != "Sunday"

if is_valid_h and is_valid_w_d:
    print("open")
else:
    print("closed")
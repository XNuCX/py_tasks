
number_of_people_n = int(input())
capacity_p = int(input())
result = number_of_people_n / capacity_p

if not number_of_people_n % capacity_p == 0:
    print(int(result) + 1)
else:
    print(int(result))
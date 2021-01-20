from math import ceil

employees_reception = 3
employee_efficiency = [int(input()) for _ in range(employees_reception)]
people_count = int(input())
count = 0
while people_count > 0:
    people_count -= sum(employee_efficiency)
    count += 1
    if count % 4 == 0:
        count += 1

print(f"Time needed: {count}h.")

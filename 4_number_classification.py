nums = input().split(", ")
print(f"Positive: {', '.join([el for el in nums if int(el) >= 0])}")
print(f"Negative: {', '.join([el for el in nums if int(el) < 0])}")
print(f"Even: {', '.join([el for el in nums if int(el) % 2 == 0])}")
print(f"Odd: {', '.join([el for el in nums if not int(el) % 2 == 0])}")
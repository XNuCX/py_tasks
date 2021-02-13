def best_list_pureness(*args):
    from collections import deque
    from sys import maxsize
    l, k = args
    l = deque(l)
    max_number = -maxsize
    rotation = 0
    if not k == 0:
        for i in range(k+1):

            sum_list = sum([el*index for index, el in enumerate(l)])
            if sum_list > max_number:
                max_number = sum_list
                rotation = i
            l.appendleft(l.pop())
    else:
        max_number = sum([el*index for index, el in enumerate(l)])
    return f"Best pureness {max_number} after {rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 0)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, -5], 0)
result = best_list_pureness(*test)
print(result)
test = ([0], 10)
result = best_list_pureness(*test)
print(result)
test = ([0,1], 10)
result = best_list_pureness(*test)
print(result)
test = ([1,0,0,0,0,0], 10)
result = best_list_pureness(*test)
print(result)
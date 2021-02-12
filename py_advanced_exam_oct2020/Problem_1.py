from collections import deque
jobs = deque([int(el) for el in input().split(", ")])
length = len(jobs)
job_index = int(input())
cycle = 0
current_min = min(jobs)
tasks_order = {}
i = 0
new_jobs = []
flag = False
indexes = []
items_left = []
while True:
    items_left = [el if i not in indexes else 10000 for i, el in enumerate(jobs) ]
    current_min = min(items_left)
    # if flag:
    #     if len(jobs) == length:
    #
    #         for i in range(len(jobs)):
    #             if jobs[i] current_min:
    #                 jobs.popleft()
    current = jobs[i]
    if current == current_min:
        cycle += current
        # tasks_order[cycle] = [i, current]
        if i == job_index:
            print(cycle)
            break
        if jobs:
            indexes.append(i)




        # else:
        #     flag = True

    # new_jobs.append(current)
    # if len(new_jobs) == length:
    #     jobs = deque([el for el in new_jobs])
    #     new_jobs = []
    if i == len(jobs) -1:
        i = 0
    else:
        i += 1




def input_(condition_, delimeter):
    contests_ = {}
    while True:
        input_data = input()
        if input_data == condition_:
            return contests_
        input_data = input_data.split(delimeter)
        if input_data[0] not in contests_:
            contests_.update({input_data[0]: [input_data[1:]]})
        else:
            contests_[input_data[0]].append(input_data[1:])


users = {}
contests = input_("end of contests", ":")
submissions = input_("end of submissions", "=>")
a = 5
for key, v in submissions.items():
    for value in v:
        flag = False
        position = 0
        if key not in contests:
            continue
        elif not value[0] == contests[key][0][0]:
            continue
        if value[1] not in users:
            users.update({value[1]:[{key: int(value[2])}]})

        else:
            for i, course in enumerate(users[value[1]]):
                if key in course:
                    position = i
                    flag = True
            if flag:
                if int(value[2]) > users[value[1]][position][key]:
                    users[value[1]][position][key] = int(value[2])
            else:
                users[value[1]].append({key: int(value[2])})

def func_sort():
    pass
for_print = []
best_score = 0
best_name = {k: v for k, v in sorted(users.items(), key=lambda x: x[0])}
# users = {k: [el for el in v] for k, v in users.items()}
count = 0
best_name_1 = ""
for key, value in best_name.items():

    temp_dict = {}
    temp_score = 0
    for v in value:

        for k_1, v_1 in v.items():
            temp_dict.update({k_1: v_1})
            temp_score += v_1
    if temp_score > best_score:
        best_score = temp_score
        best_name_1 = key
    temp_dict = {k: v for k, v in sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)}

    for_print.append(key)
    for k, v_2 in temp_dict.items():
        for_print.append(f"#  {k} -> {v_2}")
print(f"Best candidate is {best_name_1} with total {best_score} points.")
print("Ranking:")
print('\n'.join(for_print))



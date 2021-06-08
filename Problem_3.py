def flights(*args):
    flag = False
    key = ""
    final = {}
    for param in args:

        if param == "Finish":
            return final
        if flag:
            if key not in final:
                final[key] = param
            else:
                final[key] += param
            flag = False
            continue
        if type(param) is str:
            flag = True
            key = param
            continue

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
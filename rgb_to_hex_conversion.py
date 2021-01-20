def rgb(r, g, b):
    rgb_list = list(reversed([float(r), float(g), float(b)]))
    representation = []

    for i, el in enumerate(rgb_list):
        if el > 255:
            rgb_list[i] = 255
        elif el < 0:
            rgb_list[i] = 0
        if rgb_list[i] not in range(0, 16):
            while not rgb_list[i] == 0:
                if rgb_list[i] % 16 == 0:
                    representation.append(0)
                    rgb_list[i] //= 16
                else:
                    representation.append(float((rgb_list[i] / 16 - rgb_list[i] // 16) * 16))
                    rgb_list[i] //= 16

        else:
            representation.append(rgb_list[i])
            representation.append(0)

    representation = [int(el) for el in representation]
    for i in range(len(representation)):
        if representation[i] in range(10, 16):
            if representation[i] == 10:
                representation[i] = "A"
            elif representation[i] == 11:
                representation[i] = "B"
            elif representation[i] == 12:
                representation[i] = "C"
            elif representation[i] == 13:
                representation[i] = "D"
            elif representation[i] == 14:
                representation[i] = "E"
            elif representation[i] == 15:
                representation[i] = "F"
    representation = list(reversed([el for el in representation]))
    return ''.join([str(el) for el in representation])


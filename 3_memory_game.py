
won_flag = False
loose_flag = False
elements = input().split(" ")
moves = 0
command = None
flag = False
all_twins = []
count_twins = 0
current_sequence = []
for index, el in enumerate(elements):
    for sec_index, sec_el in enumerate(elements):
        if el == sec_el and index != sec_index:
            if el not in all_twins:
                all_twins.append(el)
twins_numbers = len(all_twins)
while True:
    if flag:
        if command == "end":
            if count_twins != twins_numbers:
                loose_flag = True
            break
        moves += 1
        indexes_of_elements = command.split(" ")
        indexes_of_elements = [int(el) for el in indexes_of_elements if el.isdigit() or el.lstrip("-").isdigit()]
        if not 0 <= indexes_of_elements[0] < len(elements) \
                or not 0 <= indexes_of_elements[0] < len(elements)\
                or indexes_of_elements[0] == indexes_of_elements[1]:
            middle_of_sequence = round(len(elements) / 2)
            elements.insert(middle_of_sequence, "-" + str(moves) + "a")
            elements.insert(middle_of_sequence, "-" + str(moves) + "a")
            twins_numbers += 1
            print("Invalid input! Adding additional elements to the board")
            command = input()
            continue
        if elements[indexes_of_elements[0]] == elements[indexes_of_elements[1]]:
            print(f"Congrats! You have found matching elements - {elements[indexes_of_elements[0]]}!")
            count_twins += 1
            twin = elements[indexes_of_elements[0]]
            elements = [el for el in elements if el != twin]
            if count_twins == twins_numbers:

                won_flag = True
                break
                # while True:
                #     if input() == "end":
                #         break
        else:
            print("Try again!")
    command = input()
    flag = True
if won_flag:
    print(f"You have won in {moves} turns!")
elif loose_flag:
    print(f"Sorry you lose :(\n{' '.join(elements)}")
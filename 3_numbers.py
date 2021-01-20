sequence = input().split(" ")
sequence = [int(el) for el in sequence]
average_number = sum(sequence) / len(sequence)
new_sequence = []
for _ in range(5):
    max_number = max(sequence)
    sequence.pop(sequence.index(max(sequence)))
    if max_number > average_number:
        new_sequence.append(max_number)
    if sum(new_sequence) == 0:

        print("No")
        break
# new_sequence = list(set(new_sequence))
# new_sequence.sort(reverse=True)
new_sequence = [str(el) for el in new_sequence]
print(" ".join(new_sequence))
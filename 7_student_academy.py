n = int(input())
students_data = {}
top_students = {}
for i in range(n):
    name = input()
    grade = float(input())
    if name not in students_data:
        students_data.update({name: [grade]})
    else:
        students_data[name].append(grade)

for key, value in students_data.items():
    value = sum(value)/len(value)
    if value >= 4.50:
        top_students.update({key: value})
top_students = {k: v for k, v in sorted(top_students.items(), key=lambda x: x[1], reverse=True)}
for key, value in top_students.items():
    print(f"{key} -> {value:.2f}")

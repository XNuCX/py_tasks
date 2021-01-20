command = input()
courses = {}
while not command == "end":
    command = command.split(" : ")
    course_name = command[0]
    student = command[1]
    if course_name not in courses:
        courses.update({course_name: [student]})
    else:
        courses[course_name].append(student)
    command = input()
courses = {k: v for k, v in sorted(courses.items(), key=lambda x: len(x[1]), reverse=True)}
for key, value in courses.items():
    print(f"{key}: {len(value)}")
    value = [v for v in sorted(value)]
    for v in value:
        print(f"-- {v}")

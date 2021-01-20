command = input()
company_data = {}
while not command =="End":
    command = command.split(" -> ")
    company_name = command[0]
    company_id = command[1]
    if company_name not in company_data:
        company_data.update({company_name: [company_id]})
    else:
        if company_id not in company_data[company_name]:
            company_data[company_name].append(company_id)

    command = input()

company_data = {k: v for k, v in sorted(company_data.items(), key=lambda x: x)}
for key, value in company_data.items():
    print(f"{key}")
    for ids in value:
        print(f"-- {ids}")
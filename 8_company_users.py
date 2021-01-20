command = input()
company_data = {}
series = ""
numb = ""
val = {}
while not command =="End":
    command = command.split(" -> ")
    company_name = command[0]
    company_id = command[1]
    if company_name not in company_data:
        company_data.update({company_name: {company_id}})
    else:
        company_data[company_name].add(company_id)
    command = input()

company_data = {k: v for k, v in sorted(company_data.items(), key=lambda x: x)}
for key, value in company_data.items():
    print(f"{key}")

    for item in value:
        for char in item:
            if not char.isdigit():
                series += char
            else:
                numb += char
        if series not in val:
            val.update({series: [numb]})
        else:
            val[series].append(numb)
        numb = ""
        series = ""
    for k, v in val.items():
        v = sorted(v)
        val[k] = v

    val = {k: v for k, v in sorted(val.items(), key=lambda x: x)}

    for k, v in val.items():
        #print(f"-- {k}{v}")
        for n in v:
            print(f"-- {k}{n}")
    series = ""
    numb = ""
    val = {}

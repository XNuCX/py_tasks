# import json
items_categories = dict.fromkeys(input().split(", "))
n_lines = int(input())
for _ in range(n_lines):
    category, item, *rest = input().split(" - ")
    if items_categories[category] is None:
        items_categories[category] = {item: None}
    else:
        items_categories[category].update({item: None})
    rest = [el.split(";") for el in rest]
    for el in rest:
        for it in el:
            key, val = it.split(":")
            # it = '"' + it
            # it = it.replace(":", '":')
            # it = "{" + it + "}"

            temp = {key: val}

            if items_categories[category][item] is None:
                items_categories[category][item] = temp
            else:
                items_categories[category][item].update(temp)

count = [[[items_categories[cat][item][quant] for quant in items_categories[cat][item] if quant == 'quantity'] for item in items_categories[cat]] for cat in items_categories]
qual = [[[items_categories[cat][item][qual] for qual in items_categories[cat][item] if qual == 'quality'] for item in items_categories[cat]] for cat in items_categories]

count_list = []
qual_list = []
for a in count:
    for b in a:
        for c in b:
            count_list.append(int(c))
for a in qual:
    for b in a:
        for c in b:
            qual_list.append(int(c))

count = sum(count_list)
qual = sum(qual_list) / len(items_categories)
print(f"Count of items: {count}")
print(f"Average quality: {qual:.2f}")
[print(f"{key} -> {', '.join([k for k in value])}") for key, value in items_categories.items()]
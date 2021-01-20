def first_half(mo, sm, jc):
    if not mo % 2 == 0 and mo != 1:
        sm = -(sm * 0.16)
        return sm
    elif mo % 4 == 0:
        sm = sm * 0.25
        return sm
    else:
        sm = 0
        return sm

def second_half(mo, sm, jc):
    sm = jc * 0.25
    return sm


saved_money = 0
journey_cost = float(input())
max_numb_months = int(input())
for month in range(1, max_numb_months + 1):
    saved_money += first_half(month, saved_money, journey_cost)
    saved_money += second_half(month, saved_money, journey_cost)

if saved_money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {(saved_money - journey_cost):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {(journey_cost - saved_money):.2f}lv. more.")

vacation_days = int(input())
vacation_nights = vacation_days - 1
room_type = str(input())
a = str("room for one person")
price_a = 18.00
b = str("apartment")
price_b = 25.00
c = str("president apartment")
price_c = 35.00
grade = str(input())
p = str("positive")
n = str("negative")
discount = 0
price = 0
if vacation_nights < 10:
#less than 10 days
    if room_type == a:
        discount = 0
        price = price_a
    else:
        if room_type == b:
            discount = 0.3
            price = price_b
        else:
            if room_type == c:
                discount = 0.1
                price = price_c
else:
    if vacation_nights >= 10 and vacation_nights <= 15:
#between 10 and 15 days
        if room_type == a:
            discount = 0
            price = price_a
        else:
            if room_type == b:
                discount = 0.35
                price = price_b
            else:
                if room_type == c:
                    discount = 0.15
                    price = price_c
    else:
        if vacation_nights >15:
#more than 15 days
            if room_type == a:
                discount = 0
                price = price_a
            else:
                if room_type == b:
                    discount = 0.5
                    price = price_b
                else:
                    if room_type == c:
                        discount = 0.2
                        price = price_c

price_for_stay = vacation_nights * price
price_for_stay_with_discount = price_for_stay - price_for_stay * discount

#if positive
if grade == p:
    positive_grade = price_for_stay_with_discount + price_for_stay_with_discount * 0.25
    final_price_for_stay = positive_grade
else:
    if grade == n:
#if negative
        negative_grade = price_for_stay_with_discount - price_for_stay_with_discount * 0.1
        final_price_for_stay = negative_grade

print(f"{final_price_for_stay:.2f}")
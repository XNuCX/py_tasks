longitude = int(input())
wide = int(input())
latitude = int(input())
percent_busy_volume = float(input())
busy_volume = percent_busy_volume / 100
litre = 10*10*10
total_volume = longitude * wide *latitude
result = (total_volume - (total_volume * busy_volume)) / litre
print(result)

def nb_year(p0, percent, aug, p):
    population = int(p0)
    year = 0
    while not population >= p:
        year += 1
        population += (population * percent / 100) + aug

    return year

print(nb_year(1500000, 2.5, 10000, 2000000))
def age_assignment(*args, **kwargs):
    dict_names = {}
    for name in args:
        dict_names.update({name: kwargs[name[0]]})
    return dict_names
print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
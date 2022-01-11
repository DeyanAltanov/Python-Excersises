def age_assignment(*args, **kwargs):
    assignement = {}
    for name_letter, age in kwargs.items():
        for name in args:
            if name[0] == name_letter:
                assignement[name] = age
    return assignement
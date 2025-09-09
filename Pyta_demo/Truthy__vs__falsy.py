value = [0, 0.0, None, "", [], {}, set(), -1]


def check_truthiness(value):
    for v in value:
        if v:
            print(f"{v} is Truthy")
        else:
            print(f"{v} is Falsy")


check_truthiness(value)

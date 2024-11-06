def calculate_difference(h1, h2):
    validate(h1)
    validate(h2)
    return (h1 - h2) % 24


def validate(hour):
    if hour >= 24 or hour < 0:
        raise Exception("Invalid hour")

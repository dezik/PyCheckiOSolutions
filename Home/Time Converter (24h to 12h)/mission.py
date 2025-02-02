def time_converter(time):
    hours, rest = time.split(":")
    hours = int(hours)
    rest += " p.m." if hours // 12 > 0 else " a.m."
    hours = hours % 12 if (hours != 12 and hours != 0) else 12
    return ":".join((str(hours), rest))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")

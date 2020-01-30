# MAP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
MAP = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
ONE = "I"
FIVE = "V"
TEN = "X"
FIFTY = "L"
HUNDRED = "C"
FIVE_HUNDRED = "D"
THOUSAND = "M"


def checkio(data):
    out = ""
    for k, v in MAP.items():
        if data % v != data:
            out += k
            data = data % v
    return out


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')

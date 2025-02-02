ZEROES = {"M": 1000, "C": 100, "X": 10, "I": 1}
FIVES = {"C": "D", "X": "L", "I": "V"}
NINES = {"C": "CM", "X": "XC", "I": "IX"}
FOURS = {"C": "CD", "X": "XL", "I": "IV"}

def checkio(data):
    out = ""
    for k, v in ZEROES.items():
        if data % v != data:
            period = data // v
            if period == 4: out += FOURS[k]
            elif period == 9: out += NINES[k]
            elif 4 < period < 9: out += FIVES[k] + (k * (period % 5))
            else: out += (k * (data // v))
            data = data % v
    return out


if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')

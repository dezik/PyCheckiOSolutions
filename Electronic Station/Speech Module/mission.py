FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    out = ""
    for i, n in enumerate(reversed([int(x) for x in str(number)])):
        if i == 0 and n != 0:
            out = FIRST_TEN[n - 1]
        if i == 1:
            if n == 1:
                out = SECOND_TEN[0 if out == "" else (FIRST_TEN.index(out) + 1)]
            elif n != 0:
                out = f"{OTHER_TENS[n - 2]} {out}"
        if i == 2:
            out = f"{FIRST_TEN[n - 1]} {HUNDRED} {out}"
    return out.strip()


if __name__ == '__main__':
    assert checkio(10) == 'ten', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')

import re


def long_repeat(line: str) -> int:
    if len(line) < 2:
        return len(line)
    max_len = 1
    for m in re.finditer(r"(\w)\1+", line):
        max_len = max(len(m.group()), max_len)
    return max_len


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('abababa') == 1, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

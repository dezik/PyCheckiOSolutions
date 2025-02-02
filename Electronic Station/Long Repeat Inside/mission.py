def repeat_inside(line: str):
    list_ = []
    for i in range(len(line)):
        if line.count(line[i]) == len(line):
            return line
        for j in range(i + 1, len(line)):
            first = line[i:j]
            if len(first) > len(line) / 2:
                break
            second = line[j:j + j - i]
            if first == second:
                l3 = line[i:j + j - i]
                list_.append(l3)
    out = max(list_, key=len) if list_ else ""
    return out


if __name__ == '__main__':
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')

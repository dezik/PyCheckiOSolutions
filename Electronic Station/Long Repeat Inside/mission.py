def repeat_inside(line: str):
    list_ = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            l1 = line[i:j]
            l2 = line[j:j + j]
            if l1 == l2:
                l3 = line[i:j + j]
                list_.append(l3)
    out = max(list_, key=len) if list_ else ""
    return out


# def repeat_inside(line: str):
#     map_ = {}
#     for i in range(len(line)):
#         for j in range(i + 1, len(line)):
#             l1 = line[i:j]
#             if line.count(l1) > 1:
#                 map_[l1] = line.count(l1)
#     out = ""
#     return out



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert repeat_inside('aaaaa') == 'aaaaa', "First"
    # assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')

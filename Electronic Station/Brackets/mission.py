def checkio(expression):
    stack = []
    brackets = dict(zip([")", "}", "]"], ["(", "{", "["]))
    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys() and (len(stack) == 0 or stack.pop() != brackets[char]):
            return False
    return len(stack) == 0


if __name__ == '__main__':
    assert checkio("(((1+(1+1))))]") == False, "Simple"
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

def rotate(state: list, pipe_numbers: list) -> list:
    out = []
    for i in range(len(state)):
        if is_fit(state, pipe_numbers):
            out.append(i)
        state.insert(0, state.pop())
    return out


def is_fit(state: list, pipe_numbers: list) -> bool:
    for number in set(pipe_numbers):
        if state[number] != 1:
            return False
    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"

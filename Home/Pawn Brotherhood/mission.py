def safe_pawns(pawns: set) -> int:
    count = 0
    for a, b in pawns:
        a, b = ord(a), str(int(b) - 1)
        if (chr(a + 1) + b) in pawns or (chr(a - 1) + b) in pawns:
            count += 1
    return count


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

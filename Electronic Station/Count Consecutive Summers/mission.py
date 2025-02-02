def count_consecutive_summers(num):
    count = 1
    for i in range(num // 2 + 1, 0, -1):
        for j in range(i - 1, 0, -1):
            i += j
            if i == num:
                count += 1
            elif i < num:
                continue
            break
    return count


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")

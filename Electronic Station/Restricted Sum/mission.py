def checkio(data: list):
    return data.pop() if len(data) == 1 else checkio([data.pop() + data.pop()] + data)


if __name__ == '__main__':
    print(checkio([1, 2, 3]))
    print(checkio([2, 2, 2, 2, 2, 2]))

def checkio(data: str):
    (x1, y1), (x2, y2), (x3, y3) = eval(data)

    (x1 - x) ** 2 + (y1 - y) ** 2 = r ** 2
    (x2 - x) ** 2 + (y2 - y) ** 2 = r ** 2
    (x3 - x) ** 2 + (y3 - y) ** 2 = r ** 2

    "(2,2),(6,2),(2,6)"

    (2 - x) ** 2 + (2 - y) ** 2 = (6 - x) ** 2 + (2 - y) ** 2

    (4 - 4 * x + x ** 2) + (4 - 4 * y + y ** 2) == (36 - 12 * x + x ** 2) + (4 - 4 * y + y ** 2)

    x1 ** 2 - 2 * x1 * x + x ** 2 + y1 ** 2 - 2 * y1 * y + y ** 2 = x2 ** 2 - 2 * x2 * x + x ** 2 + y2 ** 2 - 2 * y2 * y + y ** 2

    return ""


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

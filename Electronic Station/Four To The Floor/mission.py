EMPTY = " . "
FILLED = " * "


class Room:
    def __init__(self, parameters: list):
        self.width = parameters[0]
        self.height = parameters[1]
        self.coverage = [[EMPTY for _ in range(self.width)] for _ in range(self.height)]

    def get_coverage(self):
        out = ""
        for column in self.coverage:
            for line in column:
                out += line
            out += "\n"
        return out

    def cover(self, sensor: list):
        sx, sy, r = sensor
        for y in range(sy - r - 1, sy + r + 1):
            for x in range(sx - r - 1, sx + r + 1):
                if 0 <= x < self.width and 0 <= y < self.height and (((y - sy) ** 2 + (x - sx) ** 2) <= r ** 2):
                    self.coverage[y][x] = FILLED

    def is_covered(self):
        return EMPTY not in self.get_coverage()


def is_covered(room: list, sensors: list) -> bool:
    a_room = Room(room)
    for sensor in sensors:
        a_room.cover(sensor)
    return a_room.is_covered()


if __name__ == '__main__':
    assert is_covered([200, 150], [[100, 75, 130]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 60], [0, 110, 60], [200, 40, 60], [200, 110, 60]]) == True
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 50], [0, 110, 50], [200, 40, 50], [200, 110, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 110]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 20]]) == False
    assert is_covered([3, 1], [[1, 0, 2], [2, 1, 2]]) == True
    assert is_covered([30, 10], [[0, 10, 10], [10, 0, 10], [20, 10, 10], [30, 0, 10]]) == True
    assert is_covered([30, 10], [[0, 10, 8], [10, 0, 7], [20, 10, 9], [30, 0, 10]]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

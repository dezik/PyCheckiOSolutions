class Sensor:
    def __init__(self, parameters: list):
        self.x = parameters[0]
        self.y = parameters[1]
        self.r = parameters[2]


class Room:
    def __init__(self, parameters: list):
        self.width = parameters[0]
        self.height = parameters[1]
        self.coverage = [[" . " for _ in range(self.width)] for _ in range(self.height)]

    def print_coverage(self):
        print()
        for column in self.coverage:
            for line in column:
                print(line, end="")
            print()

    def cover(self, sensor: Sensor):
        pass


def is_covered(room, sensors):
    # your code here
    return True


if __name__ == '__main__':
    room = Room([15, 20])
    room.print_coverage()
    sensor = Sensor([5, 5, 5])
    room.cover(sensor)
    room.print_coverage()

    # assert is_covered([200, 150], [[100, 75, 130]]) == True
    # assert is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) == True
    # assert is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) == False
    # assert is_covered([200, 150], [[100, 75, 100], [0, 40, 60], [0, 110, 60], [200, 40, 60], [200, 110, 60]]) == True
    # assert is_covered([200, 150], [[100, 75, 100], [0, 40, 50], [0, 110, 50], [200, 40, 50], [200, 110, 50]]) == False
    # assert is_covered([200, 150], [[100, 75, 110], [105, 75, 110]]) == False
    # assert is_covered([200, 150], [[100, 75, 110], [105, 75, 20]]) == False
    # assert is_covered([3, 1], [[1, 0, 2], [2, 1, 2]]) == True
    # assert is_covered([30, 10], [[0, 10, 10], [10, 0, 10], [20, 10, 10], [30, 0, 10]]) == True
    # assert is_covered([30, 10], [[0, 10, 8], [10, 0, 7], [20, 10, 9], [30, 0, 10]]) == False
    # print("Coding complete? Click 'Check' to earn cool rewards!")

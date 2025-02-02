from typing import List


def checkio(game_result: List[str]) -> str:
    all_lines = game_result[:]
    all_lines.append("".join([all_lines[x][x] for x in range(3)]))
    all_lines.append("".join([all_lines[x][2 - x] for x in range(3)]))
    all_lines.extend(["".join([all_lines[x][y] for x in range(3)]) for y in range(3)])
    return "X" if "XXX" in all_lines else "O" if "OOO" in all_lines else "D"


if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

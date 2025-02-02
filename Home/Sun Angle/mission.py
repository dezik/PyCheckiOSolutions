def sun_angle(time: str):
    hours, minutes = map(lambda x: int(x), time.split(":"))
    minutes = (hours - 6) * 60 + minutes
    if minutes < 0 or minutes > 720:
        return "I don't see the sun!"
    return round(minutes / 4, 2)


if __name__ == '__main__':
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

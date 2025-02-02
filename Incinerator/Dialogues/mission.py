VOWELS = "aeiou"


class User:
    def __init__(self, name: str):
        self.name = name

    def send(self, s: str):
        self._dialogue.append(self.name + " said: " + s)

    def _add_to_chat(self, dialogue: list):
        self._dialogue = dialogue


class Human(User):
    def __init__(self, name: str):
        super().__init__(name)


class Robot(User):
    def __init__(self, serial_number: str):
        super().__init__(serial_number)


class Chat:
    def __init__(self):
        self.dialogue = []

    def connect_human(self, human: Human):
        human._add_to_chat(self.dialogue)

    def connect_robot(self, robot: Robot):
        robot._add_to_chat(self.dialogue)

    def show_human_dialogue(self):
        return "\n".join(self.dialogue)

    def show_robot_dialogue(self):
        robo_dialog = []
        for line in self.dialogue:
            parts = line.split(": ")
            robo_dialog.append(parts[0] + ": " + "".join(["0" if x in VOWELS else "1" for x in parts[1]]))
        return "\n".join(robo_dialog)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")

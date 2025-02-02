VOWELS = "aeiouy"


def translate(phrase):
    for vowel in VOWELS:
        phrase = phrase.replace(vowel * 3, vowel)
    i = 0
    while len(phrase) > i:
        if phrase[i] not in VOWELS and phrase[i] != " ":
            phrase = phrase[:i + 1] + phrase[i + 2:]
        i += 1
    return phrase


if __name__ == '__main__':
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

import re


def has_marker_word(word, subj):
    union = set(word) & set(subj.lower())
    return union == set(word)


def is_stressful(subj: str) -> bool:
    """
        recognize stressful subject
    """
    marker_words = ("help", "asap", "urgent")
    if re.match(r".*!{3,}$", subj):
        return True
    if subj.upper() == subj:
        return True
    for word in marker_words:
        if has_marker_word(word, subj):
            return True
    return False


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')

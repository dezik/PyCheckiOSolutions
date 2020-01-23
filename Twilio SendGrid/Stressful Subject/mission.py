import re


def is_stressful(subj: str) -> bool:
    if subj.isupper() or subj.endswith("!!!"):
        return True
    subj = re.sub("[^a-z]", "", subj.lower())
    for match in re.finditer(r"(\w)\1+", subj):
        subj = subj.replace(match.group(), match.group(1))
    return any(x in subj for x in ("help", "asap", "urgent"))


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')

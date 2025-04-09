"""Houses function skeletons and implementations"""

__author__: str = "730608493"


def invert(initial: dict[str, str]) -> dict[str, str]:
    """Switches key and value positions in a str dictionary"""
    inverted: dict[str, str] = {}
    for key in initial:
        if initial[key] in inverted:
            raise KeyError("Duplicate keys")
        else:
            inverted[initial[key]] = key
    return inverted


def count(list: list[str]) -> dict[str, int]:
    """Counts the number of times each item appears in a list"""
    occurrences: dict[str, int] = {}
    item: str
    idx: int = 0
    for item in list:
        item = list[idx]
        if item in occurrences:
            occurrences[item] = occurrences[item] + 1
        else:
            occurrences[item] = 1
        idx += 1
    return occurrences


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most popular favorite color found in given dict"""
    occurrences: dict[str, int] = {}
    for name in colors:
        color = colors[name]
        if color in occurrences:
            occurrences[color] += 1
        else:
            occurrences[color] = 1
    winner: str = ""
    tally: int = 0
    for color in occurrences:
        if occurrences[color] > tally:
            tally = occurrences[color]
            winner = color
    return winner


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """Creates a dictionary displaying the length of strings in a list"""
    result: dict[int, set[str]] = {}
    for item in strings:
        if len(item) not in result:
            result[len(item)] = {item}
        else:
            result[len(item)].add(item)
    return result

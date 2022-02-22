from collections import defaultdict


def is_anagram(first_string, second_string):
    anagram = defaultdict(int)
    if len(first_string) != len(second_string):
        return False
    for char in first_string:
        anagram[char] += 1
    for char in second_string:
        anagram[char] -= 1
        if anagram[char] < 0:
            return False
    return True

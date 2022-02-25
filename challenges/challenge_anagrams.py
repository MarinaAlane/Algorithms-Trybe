def build_counts(string):
    words = dict()
    for l in string:
        words[l] = words.setdefault(l, 0) + 1

    return words


def is_anagram(string1, string2):
    word1 = build_counts(string1)
    word2 = build_counts(string2)

    return word1 == word2

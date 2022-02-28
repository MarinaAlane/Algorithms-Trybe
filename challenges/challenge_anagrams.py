def counter(string):
    return {i: string.count(i) for i in set(string)}


def is_anagram(first_string, second_string):
    if counter(first_string) == counter(second_string):
        return True
    return False

# https://stackoverflow.com/questions/48217471/is-it-possible-to-check-for-anagram-without-using-sorted-or-dictionary-that-pe

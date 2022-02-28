def count_string(word):
    string = dict()

    for letter in word:
        try:
            string[letter] += 1
        except KeyError:
            string[letter] = 1
    return string


def is_anagram(first_string, second_string):
    if count_string(first_string) == count_string(second_string):
        return True
    else:
        return False

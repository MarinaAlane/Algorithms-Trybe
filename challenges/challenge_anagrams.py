def create_dict(word, word2):
    count = dict()
    for i in word:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return verify_second_word(count, word2)


def verify_second_word(word_dict, word2):
    for i in word2:
        if i not in word_dict:
            return False
        if word_dict[i] == 0:
            return False
        if i in word2:
            word_dict[i] -= 1
        else:
            return False

    return True


def is_anagram(first_string, second_string):
    try:
        if len(first_string) < 2 or len(second_string) < 2:
            return False

        if len(first_string) != len(second_string):
            return False

        first_string = first_string.lower()
        second_string = second_string.lower()

        return create_dict(first_string, second_string)

    except ValueError:
        return False

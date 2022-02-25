# https://www.geeksforgeeks.org/python-program-to-check-whether-two-strings-are-anagram-of-each-other/?ref=rp]
# https://www.geeksforgeeks.org/ord-function-python/


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    num_character = 256

    count1 = [0] * num_character
    count2 = [0] * num_character

    for i in first_string:
        count1[ord(i)] += 1
    for i in second_string:
        count2[ord(i)] += 1
    for i in range(num_character):
        if count1[i] != count2[i]:
            return False
    return True

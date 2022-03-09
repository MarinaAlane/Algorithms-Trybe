"""
SOURCE: 
https://stackoverflow.com/questions/11964450
/python-order-a-list-of-numbers-without-built-in-sort-min-max-function
"""
def ordening(word):
    word_listed = list(word)
    ordened_list = []

    while len(word_listed) != 0:
        first_letter = word_listed[0]

        for letter in word_listed:
            if letter < first_letter:
                first_letter = letter
        ordened_list.append(first_letter)
        word_listed.remove(first_letter)
    
    return ''.join(ordened_list)


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return False

    if len(first_string) != len(second_string):
        return False

    fs_ordened = ordening(first_string)
    ss_ordened = ordening(second_string)
    print(fs_ordened)
    print(ss_ordened)

    if fs_ordened != ss_ordened:
        return False

    return True

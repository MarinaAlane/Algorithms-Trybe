def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if len(first_string) != len(second_string):
        return False

    array = [letter for letter in first_string]

    for letter in second_string:
        if letter not in array:
            return False
        array.remove(letter)

    return True


if __name__ == '__main__':
    result = is_anagram('edu', 'ude')
    print(result)

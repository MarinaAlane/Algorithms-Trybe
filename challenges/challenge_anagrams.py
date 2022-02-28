def is_anagram(first_string, second_string):
    for letter in second_string:
        if letter not in first_string:
            return False

    return True


if __name__ == '__main__':
    result = is_anagram('edu', 'ude')
    print(result)

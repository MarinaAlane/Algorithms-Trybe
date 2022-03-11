def is_anagram(first_string, second_string):
    a = list(first_string)
    b = list(second_string)
    if a == b:
        return True
    else:
        return False


print(is_anagram('pedra', 'perdaaa'))

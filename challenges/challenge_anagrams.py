#teste
def is_anagram(first_string, second_string):
    if len(first_string) or len(second_string) == 0:
        return False
    if len(first_string) is not len(second_string):
        return False

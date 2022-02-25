# Source: https://stackoverflow.com/questions/52717742/how-to-sort-a-string-\
# into-alphabetical-order-without-inbuilt-functions
def sort(string):
    if not string:
        return []
    return (
        sort([letter for letter in string[1:] if letter < string[0]])
        + [string[0]] +
        sort([letter for letter in string[1:] if letter >= string[0]])
    )


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    if not len(first_string) == len(second_string):
        return False

    first_string = ''.join(sort(first_string))
    second_string = ''.join(sort(second_string))

    if first_string == second_string:
        return True

    return False

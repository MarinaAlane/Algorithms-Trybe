def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    for letter in first_string:
        if first_string.count(letter) != second_string.count(letter):
            return False

    return True

def is_anagram(first_string, second_string):
    string_validy = (first_string == "" or second_string == "")
    length_validy = len(first_string) != len(second_string)
    if string_validy or length_validy:
        return False

def get_char_schema(string):
    schema = dict()

    for char in string:
        try:
            schema[char] += 1
        except KeyError:
            schema[char] = 1

    return schema


def is_anagram(first_string, second_string):
    first_char_schema = get_char_schema(first_string)
    second_char_schema = get_char_schema(second_string)

    return first_char_schema == second_char_schema

# https://github.com/tryber/sd-011-project-algorithms/pull/91
# https://github.com/tryber/sd-011-project-algorithms/pull/97


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    for le in first_string:
        second_string = second_string.replace(le, '', 1)

    return second_string == ''

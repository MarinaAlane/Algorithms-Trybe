def is_anagram(first_string, second_string):
    if valid_anagram(split(first_string)) == valid_anagram(split(second_string)):
        return True
    else:
        return False

"""Miguel campos me ajudou na complexidade dessa questão"""

def split(word):
    return [char for char in word]


def valid_anagram(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return valid_anagram(items_lower) + [pivot] + valid_anagram(items_greater)


def split(word):
    return [char for char in word]

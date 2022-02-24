def is_anagram(first_string, second_string):
    firstWorldDictionary = dict()
    secondWorldDictionary = dict()

    for character in first_string:
        firstWorldDictionary[character] = firstWorldDictionary.get(character, 0) + 1
    for character in second_string:
        secondWorldDictionary[character] = secondWorldDictionary.get(character, 0) + 1

    return firstWorldDictionary == secondWorldDictionary

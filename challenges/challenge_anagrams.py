def is_anagram(first_string, second_string):
    # https://www.javatpoint.com/python-dict-function
    firstWord = dict()
    secondWord = dict()

    for letter in first_string:
        firstWord[letter] = firstWord.get(letter, 0) + 1
    for letter in second_string:
        secondWord[letter] = secondWord.get(letter, 0) + 1

    return firstWord == secondWord

def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    
    matchedChars = 0
    
    for char in first_string:
        if char in second_string:
            matchedChars += 1
            second_string = second_string.replace(char, '', 1)
    
    return matchedChars == len(first_string)
